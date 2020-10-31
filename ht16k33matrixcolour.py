from ht16k33 import HT16K33

class HT16K33MatrixColour(HT16K33):
    """
    Micro/Circuit Python class for the Adafruit 8x8 bi-colour LED matrix
    backpack.

    Version:    3.0.0
    Bus:        I2C
    Author:     Tony Smith (@smittytone)
    License:    MIT
    """

    # *********** CONSTANTS **********

    COLOUR_NONE = 0
    COLOUR_GREEN = 1
    COLOUR_RED = 2
    COLOUR_YELLOW = 3

    CHARSET = [
        b"\x00\x00",              # space - Ascii 32
        b"\xfa",                  # !
        b"\xc0\x00\xc0",          # "
        b"\x24\x7e\x24\x7e\x24",  # #
        b"\x24\xd4\x56\x48",      # $
        b"\xc6\xc8\x10\x26\xc6",  # %
        b"\x6c\x92\x6a\x04\x0a",  # &
        b"\xc0",                  # '
        b"\x7c\x82",              # (
        b"\x82\x7c",              # )
        b"\x10\x7c\x38\x7c\x10",  # *
        b"\x10\x10\x7c\x10\x10",  # +
        b"\x06\x07",              # ,
        b"\x10\x10\x10\x10",      # -
        b"\x06\x06",              # .
        b"\x04\x08\x10\x20\x40",  # /
        b"\x7c\x8a\x92\xa2\x7c",  # 0 - Ascii 48
        b"\x42\xfe\x02",          # 1
        b"\x46\x8a\x92\x92\x62",  # 2
        b"\x44\x92\x92\x92\x6c",  # 3
        b"\x18\x28\x48\xfe\x08",  # 4
        b"\xf4\x92\x92\x92\x8c",  # 5
        b"\x3c\x52\x92\x92\x8c",  # 6
        b"\x80\x8e\x90\xa0\xc0",  # 7
        b"\x6c\x92\x92\x92\x6c",  # 8
        b"\x60\x92\x92\x94\x78",  # 9
        b"\x36\x36",              # : - Ascii 58
        b"\x36\x37",              #
        b"\x10\x28\x44\x82",      # <
        b"\x24\x24\x24\x24\x24",  # =
        b"\x82\x44\x28\x10",      # >
        b"\x60\x80\x9a\x90\x60",  # ?
        b"\x7c\x82\xba\xaa\x78",  # @
        b"\x7e\x90\x90\x90\x7e",  # A - Ascii 65
        b"\xfe\x92\x92\x92\x6c",  # B
        b"\x7c\x82\x82\x82\x44",  # C
        b"\xfe\x82\x82\x82\x7c",  # D
        b"\xfe\x92\x92\x92\x82",  # E
        b"\xfe\x90\x90\x90\x80",  # F
        b"\x7c\x82\x92\x92\x5c",  # G
        b"\xfe\x10\x10\x10\xfe",  # H
        b"\x82\xfe\x82",          # I
        b"\x0c\x02\x02\x02\xfc",  # J
        b"\xfe\x10\x28\x44\x82",  # K
        b"\xfe\x02\x02\x02",      # L
        b"\xfe\x40\x20\x40\xfe",  # M
        b"\xfe\x40\x20\x10\xfe",  # N
        b"\x7c\x82\x82\x82\x7c",  # O
        b"\xfe\x90\x90\x90\x60",  # P
        b"\x7c\x82\x92\x8c\x7a",  # Q
        b"\xfe\x90\x90\x98\x66",  # R
        b"\x64\x92\x92\x92\x4c",  # S
        b"\x80\x80\xfe\x80\x80",  # T
        b"\xfc\x02\x02\x02\xfc",  # U
        b"\xf8\x04\x02\x04\xf8",  # V
        b"\xfc\x02\x3c\x02\xfc",  # W
        b"\xc6\x28\x10\x28\xc6",  # X
        b"\xe0\x10\x0e\x10\xe0",  # Y
        b"\x86\x8a\x92\xa2\xc2",  # Z - Ascii 90
        b"\xfe\x82\x82",          # [
        b"\x40\x20\x10\x08\x04",  # \
        b"\x82\x82\xfe",          # ]
        b"\x20\x40\x80\x40\x20",  # ^
        b"\x02\x02\x02\x02\x02",  # _
        b"\xc0\xe0",              # '
        b"\x04\x2a\x2a\x1e",      # a - Ascii 97
        b"\xfe\x22\x22\x1c",      # b
        b"\x1c\x22\x22\x22",      # c
        b"\x1c\x22\x22\xfc",      # d
        b"\x1c\x2a\x2a\x10",      # e
        b"\x10\x7e\x90\x80",      # f
        b"\x18\x25\x25\x3e",      # g
        b"\xfe\x20\x20\x1e",      # h
        b"\xbc\x02",              # i
        b"\x02\x01\x21\xbe",      # j
        b"\xfe\x08\x14\x22",      # k
        b"\xfc\x02",              # l
        b"\x3e\x20\x18\x20\x1e",  # m
        b"\x3e\x20\x20 \x1e",     # n
        b"\x1c\x22\x22\x1c",      # o
        b"\x3f\x22\x22\x1c",      # p
        b"\x1c\x22\x22\x3f",      # q
        b"\x22\x1e\x20\x10",      # r
        b"\x12\x2a\x2a\x04",      # s
        b"\x20\x7c\x22\x04",      # t
        b"\x3c\x02\x02\x3e",      # u
        b"\x38\x04\x02\x04\x38",  # v
        b"\x3c\x06\x0c\x06\x3c",  # w
        b"\x22\x14\x08\x14\x22",  # x
        b"\x39\x05\x06\x3c",      # y
        b"\x26\x2a\x2a\x32",      # z - Ascii 122
        b"\x10\x7c\x82\x82",      #
        b"\xee",                  # |
        b"\x82\x82\x7c\x10",      #
        b"\x40\x80\x40\x80",      # ~
        b"\x60\x90\x90\x60"       # Degrees sign - Ascii 127
    ]

    # ********** PRIVATE PROPERTIES **********

    width = 8
    height = 8
    def_chars = None
    rotation_angle = 0
    is_rotated = False
    is_inverse = False

    # *********** CONSTRUCTOR **********

    def __init__(self, i2c, i2c_address=0x70):
        self.buffer = bytearray(self.width * 2)
        self.def_chars = []
        for i in range(32): self.def_chars.append(b"\x00")
        super(HT16K33MatrixColour, self).__init__(i2c, i2c_address)

    # *********** PUBLIC METHODS **********

    def set_angle(self, angle=0):
        """
        Set the matrix orientation

        Args:
            angle (integer) Display auto-rotation angle, 0 to -360 degrees. Default: 0

        Returns:
            The instance (self)
        """
        # Bring the supplied angle to with 0-360 degrees
        if angle > 360:
            while angle > 360:
                angle -= 360

        if angle < 0:
            while angle < 360:
                angle += 360

        # Convert angle to internal value:
        # 0 = none, 1 = 90 clockwise, 2 = 180, 3 = 90 anti-clockwise
        if angle > 3:
            if angle < 45 or angle > 360: angle = 0
            if angle >= 45 and angle < 135: angle = 1
            if angle >= 135 and angle < 225: angle = 2
            if angle >= 225: angle = 3

        self.rotation_angle = angle
        self.is_rotated = True if self.rotation_angle != 0 else False
        return self

    def set_icon(self, glyph, ink, paper, centre=False):
        """
        Displays a custom character on the matrix

        Args:
            glyph (array) 1-8 8-bit values defining a pixel image. The data is passed as columns
                          0 through 7, left to right. Bit 0 is at the bottom, bit 7 at the top
            ink (int)     The colour of the pixels
            paper (int)   The colour of the background
            centre (bool) Whether the icon should be displayed centred on the screen. Default: False

        Returns:
            The instance (self)
        """
        length = len(glyph)
        assert length < 1 or length > self.width, "ERROR - Invalid glyph set in set_icon:"
        offset = (8 - length) // 2
        for i in range(length):
            col = glyph[i]
            for y in range(8):
                if col & (1 << y):
                    self.plot(a + x, y, ink)
                else:
                    self.plot(a + x, y, paper)
        return self

    def set_character(self, ascii_value=32, centre=False):
        """
        Display a single character specified by its Ascii value on the matrix

        Args:
            ascii_value (integer) Character Ascii code. Default: 32 (space)
            centre (bool)         Whether the icon should be displayed centred on the screen. Default: False

        Returns:
            The instance (self)
        """
        glyph = None
        if ascii_value < 32:
            # A user-definable character has been chosen
            glyph = self.def_chars[ascii_value]
        else:
            # A standard character has been chosen
            ascii_value -= 32
            if ascii_value < 0 or ascii_value >= len(self.CHARSET): ascii_value = 0
            glyph = self.charset[ascii_value]
        return self.set_icon(glyph, centre)

    def scroll_text(self, the_line, speed=0.1):
        """
        Scroll the specified line of text leftwards across the display.

        Args:
            the_line (string) The string to display
            speed (float)     The delay between frames

        Returns:
            None on error
        """
        import time

        if the_line is None or len(the_line) == 0: return None
        the_line += "    "

        # Calculate the source buffer size
        length = 0
        for i in range(0, len(the_line)):
            asc_val = ord(the_line[i])
            if asc_val < 32:
                glyph = self.def_chars[asc_val]
            else:
                glyph = self.CHARSET[asc_val - 32]
            length += len(glyph) + 1
        src_buf = bytearray(length * 8)

        # Draw the string to the source buffer
        row = 0
        for i in range(0, len(the_line)):
            asc_val = ord(the_line[i])
            if asc_val < 32:
                glyph = self.def_chars[asc_val]
            else:
                glyph = self.CHARSET[asc_val - 32]
            for j in range(0, len(glyph)):
                src_buf[row] = glyph[j] if self.is_inverse is False else ((~ glyph[j]) & 0xFF)
                row += 1
            row += 1

        # Finally, nimate the line
        row = 0
        cur = 0
        while row < length:
            for i in range(0, self.width):
                self.buffer[i] = src_buf[cur];
                cur += 1
            self.draw()
            time.sleep(speed)
            row += 1
            cur -= (self.width - 1)

    def define_character(self, glyph, char_code=0):
        """
        Set a user-definable character for later use

        Args:
            glyph (bytearray)   1-8 8-bit values defining a pixel image. The data is passed as columns,
                                with bit 0 at the bottom and bit 7 at the top
            char_code (integer) Character's ID Ascii code 0-31. Default: 0
        """
        if glyph == None or len(glyph) == 0 or len(glyph) > self.width: return None
        if 0 <= char_code < 32:
            self.def_chars[char_code] = glyph
            return self
        return None

    def plot(self, x, y, ink=1, xor=False):
        """
        Plot a point on the matrix. (0,0) is bottom left as viewed

        Args:
            x (integer)   X co-ordinate (0 - 7) left to right
            y (integer)   Y co-ordinate (0 - 7) bottom to top
            ink (integer) Pixel color: 1 = 'white', 0 = black. NOTE inverse video mode reverses this. Default: 1
            xor (bool)    Whether an underlying pixel already of color ink should be inverted. Default: False

        Returns:
            The instance (self) or None on error
        """
        # Check argument range and value
        assert (0 <= x < self.width) and (0 <= y < self.height), "ERROR - Invalid coordinate set in plot:"
        if ink not in (0, 1, 2, 3): ink = 1
        for i in range(2):
            a = x * 2 + i
            v = self.buffer[a]
            c = ink & (1 << i)
            if c != 0:
                v |= (1 << y)
            else:
                v &= ~(1 << y)
            self.buffer[a] = v
        return self

    def is_set(self, x, y):
        """
        Indicate whether a pixel is set.

        Args:
            x (integer) X co-ordinate left to right
            y (integer) Y co-ordinate bottom to top

        Returns:
            Whether the pixel is set (True) or not (False), or None on error
        """
        assert (0 <= x < self.width) and (0 <= y < self.height), "ERROR - Invalid coordinate set in is_set:"
        val_left = self.buffer[x]
        val_right = self.buffer[x + 1]
        bit = ((val_left >> y) & 1) or ((val_right >> y) & 1)
        return bit

    def fill(self, ink):
        """
        Fill the matrix with the specified colour.

        Args:
            colour (integer) The chosen colour (0, 1, 2, 3)

        Returns:
            The instance (self)
        """
        assert ink in (0, 1, 2, 3), "ERROR - Invalid colour set in fill:"
        for i in range(0, 15, 2):
            self.buffer[i] = ((ink >> 1) & 0x01) * 0xFF
            self.buffer[i + 1] = (ink & 0x01) * 0xFF
        return self

    def draw(self):
        """
        Takes the contents of _buffer and writes it to the LED matrix.
        NOTE Overrides the parent method
        """
        draw_buffer = bytearray(17)
        new_buffer = bytearray(16)
        if self.is_rotated:
            new_buffer = self._rotate_matrix(self.buffer, self.rotation_angle)
            for i in range(len(new_buffer)):
                draw_buffer[i + 1] = new_buffer[i]
        else:
            for i in range(len(self.buffer)):
                draw_buffer[i + 1] = self.buffer[i]
        self.i2c.writeto(self.address, bytes(draw_buffer))

    # ********** PRIVATE METHODS **********

    def _rotate_matrix(self, input_matrix, angle=0):
        """
        Rotate an 16-integer matrix through the specified angle in 90-degree increments:
        0 = none, 1 = 90 clockwise, 2 = 180, 3 = 90 anti-clockwise
        BUT maintain adjacent column pairs
        """
        assert angle in (0, 1, 2, 3), "ERROR -- Invalid angle set in _rotate_matrix:"
        if angle is 0: return input_matrix

        # NOTE It's quicker to have three case-specific
        #      code blocks than a single, generic block
        output_matrix = bytearray(self.width * 2)
        for x in range(0, 15, 2):
            val_left = buffer[x]
            val_right = buffer[x + 1]
            for y in range(8):
                if angle == 1:
                    if (val_left >> y) & 1:
                        output_matrix[y * 2] |= (1 << (7 - (x // 2)))
                    if (val_right >> y) & 1:
                        output_matrix[y * 2 + 1] |= (1 << (7 - (x // 2)))
                elif angle == 2:
                    if (val_left >> y) & 1:
                        output_matrix[14 - x] |= (1 << (7 - y))
                    if (val_right >> y) & 1:
                        output_matrix[15 - x] |= (1 << (7 - y))
                else:
                    if (val_left >> y) & 1:
                        output_matrix[14 - y * 2] |= (1 << (x // 2))
                    if (val_right >> y) & 1:
                        output_matrix[15 - y * 2] |= (1 << (x // 2))
        return output_matrix