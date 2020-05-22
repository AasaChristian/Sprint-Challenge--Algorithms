

class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):

        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        
        return self._position < len(self._list) - 1
        

    def can_move_left(self):

        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            # print("Moved RIGHT 46")
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            # print("Moved LEFT 60")
            return True
        else:
            return False

    def swap_item(self):
        # print("swap 66", self._item, "Item", self._list[self._position], "position")
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            # print("compare Item is None 85")
            # print(self._item, "self.Item")
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"



    def sort(self):
    # helper function that swaps the None value item with the first position
    # moves to the next position
    # calls function to start sorting list
    # this `sort` function is called once
        self.swap_item()
        self.move_right()
        self.sort2()

    def sort2(self):
        # loop run intill light is on is true
        while self.light_is_on() == False:
        # checks if there is a position to the right
            if self.can_move_right() == True:
                # check if item is less than position
                # if item is less than value of the position
                # swap the item and position value
                # then move to the next position on the right
                if self.compare_item() == -1:
                    self.swap_item()
                    self.move_right()
                # if item is greater than position value
                # move to the next position on the right
                elif self.compare_item() == 1:
                    self.move_right()
                # else means there is no postion to the right/ the last item in the list
            else:
                # if the item is less than position value
                if self.compare_item() == -1:
                # this loop finds the smallest value and moves it to the front of the list
                # the loop will continue intill it reaches the position with the None value
                    while self.compare_item() != None:
                # if the item is less than position value move to the position on the left
                        if self.compare_item() == -1:
                            self.move_left()
                # if the item is greater than position value, swap the item and position value
                # move to position on the left
                        else:
                            self.swap_item()
                            self.move_left()
                # the loops stops when the compared position value is None
                # the lowest value swapps None value at that position
                # the None valued item moves to the position to the right 
                # the None valued item swaps with the position and moves to the position to the right
                # this locks the already sorted value(s) to the left of the None valued position
                    self.swap_item()
                    self.move_right()
                    self.swap_item()
                    self.move_right()
                # if the item is greater than position value

                elif self.compare_item() == 1:
                # swap the item and position
                    self.swap_item()
                # this loop finds the smallest value and moves it to the front of the list
                # the loop will continue intill it reaches the position with the None value
                    while self.compare_item() != None:
                # if the item is less than position value move to the position on the left
                        if self.compare_item() == -1:
                            self.move_left()
                # if the item is greater than position value, swap the item and position value
                # move to position on the left
                        else:
                            self.swap_item()
                            self.move_left()
                # the loops stops when the compared position value is None
                # the lowest value swapps None value at that position
                # the None valued item moves to the position to the right 
                # the None valued item swaps with the position and moves to the position to the right
                # this locks the already sorted value(s) to the left of the None valued position
                    self.swap_item()
                    self.move_right()
                    self.swap_item()
                    self.move_right()
                # if the compare values is None and there are no positions to the right
                # the position(s) to the left of the None value position is/are sorted
                # if the none value position is the last position that mean the list is sorted
                # swap the item value with None value at the last position
                # set the light on that breaks the while loop
                else:
                    self.swap_item()
                    self.set_light_on()
                # once the loop is completed return self/the list
        return self

    # def go_back(self):
    #     if self.compare_item() == None:
    #         # if self.light_is_on() == False:
    #         #     self.swap_item()
    #         #     # print("end")
    #         #     return self
    #         # else:
    #             self.swap_item()
    #             self.move_right()
    #             self.swap_item()
    #             self.set_light_on()
    #             self.move_right()
    #             # print("118")
    #             self.sort2()

    #     elif self.compare_item() == -1:
    #         self.move_left()
    #         # print("124")
    #         self.go_back()

    #     else:
    #         self.swap_item()
    #         self.set_light_on()
    #         self.move_left()
    #         # print("131")
    #         self.go_back()


    # def sort(self):
    #     self.swap_item()
    #     self.move_right()
    #     # print("138")
    #     self.sort2()

    # def sort2(self):
    #     if self.can_move_right() == True:
    #         if self.compare_item() == -1:
    #             self.swap_item()
    #             self.set_light_on()
    #             self.move_right()
    #             # print("147")
    #             self.sort2()

    #         elif self.compare_item() == 1:
    #             self.move_right()
    #             # print("154")
    #             self.sort2()

    #     else:
    #         if self.compare_item() == -1:
    #             self.set_light_off()
    #             # print("160")
    #             self.go_back()

    #         elif self.compare_item() == 1:
    #             self.swap_item()
    #             self.set_light_off()
    #             # print("167")
    #             self.go_back()
    #         else:
    #             self.swap_item()
        
    #             return self

if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`
    # l = [1, -38, -95, 4, 23, -73, -65, -36, 85, 2, 58, -26, -55, 96, 55, -76, 64, 45, 69, 36, 69, 47, 29, -47, 13, 89, -57, -88, -87, 54, 60, 56, -98, -78, 59, 93, -41, -74, 73, -35, -23, -79, -35, 46, -18, -18, 37, -64, 14, -57, -2, 15, -85, 45, -73, -2, 79, -87, -100, 21, -51, 22, 26, -59, 81, 59, -24, 24, -81, 43, 61, 52, 38, -88, -95, 87, -57, -37, -65, -47, -3, 21, -77, 98, 25, 1, -36, 39, 78, 47, -35, -40, -69, -81, 11, -47, 21, 25, -53, -31]
    # l = [11, 13, 7, 17, 9, 20, 1, 21, 2, 4, 22, 16, 15, 10, 23, 19, 8, 3, 5, 14, 6, 0, 24, 12, 18, 1 ]
    l = [5, 4, 3, 2, 1]
    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)