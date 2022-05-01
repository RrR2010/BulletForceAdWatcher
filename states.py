from abc import ABC
import pyautogui
from imgs import IMG_PATHS
from time import sleep


class State(ABC):
    def run(self):
        ...


class OpeningFreeWeapon(State):
    def __init__(self, context):
        self.context = context

    def run(self):
        print('Searching for "Free Weapon" button')
        free_weapon = pyautogui.locateOnScreen(IMG_PATHS.FREE_WEAPON)
        if free_weapon:
            pyautogui.click(pyautogui.center(free_weapon),
                            tween=pyautogui.easeInOutCubic, duration=0.5)
            sleep(1)
            self.context.state = self.context.opening_credits


class OpeningFreeCredits(State):
    def __init__(self, context):
        self.context = context

    def run(self):
        print('Searching for "Get FREE Credits or Random Skins" button')
        free_credits = pyautogui.locateOnScreen(IMG_PATHS.FREE_CREDITS, confidence=0.95)
        if free_credits:
            pyautogui.click(pyautogui.center(free_credits),
                            tween=pyautogui.easeInOutCubic, duration=0.5)
            sleep(1)
            self.context.state = self.context.jump_ads


class JumpAdsOrWait(State):
    def __init__(self, context):
        self.context = context

    def run(self):
        print('Searching for "Skip AD" or "Continue" buttons')
        for skip_ad_path in IMG_PATHS.SKIP_AD:
            skip_ad = pyautogui.locateOnScreen(skip_ad_path, confidence=0.8)
            if skip_ad:
                pyautogui.click(pyautogui.center(skip_ad),
                                tween=pyautogui.easeInOutCubic, duration=0.5)
                sleep(1)
                self.context.state = self.context.confirm_box_opened
        closed_box = pyautogui.locateOnScreen(IMG_PATHS.BOX_CLOSED, confidence=0.9)
        if closed_box:
            sleep(1)
            self.context.state = self.context.confirm_box_opened


class ConfirmBoxOpened(State):
    def __init__(self, context):
        self.context = context
        self.is_box_opened = False

    def run(self):
        print('Waiting for box open and searching for "Done" button')
        if not self.is_box_opened:
            box_opened = pyautogui.locateOnScreen(IMG_PATHS.BOX_OPENED, confidence=0.8)
            if box_opened:
                self.is_box_opened = True
        if self.is_box_opened:
            done = pyautogui.locateOnScreen(IMG_PATHS.DONE)
            if done:
                self.is_box_opened = False
                pyautogui.click(pyautogui.center(done),
                                tween=pyautogui.easeInOutCubic, duration=0.5)
                print("Waiting 100 seconds")
                sleep(100)
                self.context.state = self.context.opening_weapon
