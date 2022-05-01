from states import State, OpeningFreeWeapon, OpeningFreeCredits, JumpAdsOrWait, ConfirmBoxOpened
import pyautogui


class MainLoop:
    def __init__(self):
        self.initialize_states()
        self.state = self.opening_weapon

    def initialize_states(self):
        self.opening_weapon = OpeningFreeWeapon(self)
        self.opening_credits = OpeningFreeCredits(self)
        self.jump_ads = JumpAdsOrWait(self)
        self.confirm_box_opened = ConfirmBoxOpened(self)

    @property
    def state(self):
        return self._state

    @state.setter
    def state(self, state: State):
        self._state = state
        print(f"Changing to state {self._state}")

    def loop(self):
        try:
            while True:
                self.state.run()
                pyautogui.press("ctrl")
        except KeyboardInterrupt as err:
            raise err


if __name__ == "__main__":
    loop = MainLoop()
    loop.loop()
