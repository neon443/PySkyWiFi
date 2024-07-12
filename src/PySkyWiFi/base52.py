<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> master
#the order of the chars is  uppercase A-Z, lowercase a-z
    # ASCII:
        # a-z 97-122
        # A-Z 65-90

def b52_encode(input_string):
<<<<<<< HEAD
=======
=======
def b26_encode(input_string):
>>>>>>> master
>>>>>>> master
    # Convert input string to a base-256 integer
    base256_int = 0
    for char in input_string:
        base256_int = base256_int * 256 + ord(char)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> master

    # Special case for empty input or input that equals zero
    if base256_int == 0:
        return 'A'

    # Convert base-256 integer to base-52 string
    base52_str = ""
    while base256_int > 0:
        remainder = base256_int % 52
        # divides by 52 and sets 'remainder' to the remainder of the division
        # this allows us to get the char we need to handle next:
        # if remainder is < 26, it has to be uppercase,
        # if remainder is > 26, it must be lowercase
        # so we can handle the base52_str additions correctly
        if remainder < 26:
            base52_str = chr(remainder + 65) + base52_str  # A-Z
        else:
            base52_str = chr(remainder - 26 + 97) + base52_str  # a-z
        base256_int //= 52 # divides by 52, reducing by the digit just handled
    return base52_str


def b52_decode(input_string):
    # Convert base-52 string to a base-256 integer
    base52_int = 0
    for char in input_string:
        # b52Int gets * 52 to shift one up, then the ascii val is added
        # but the start ascii value is deducted
        # for lc (lowercase) it has to be - 97 + 26 bc lc starts at ASCII 97 and starts at b52 26
        if 'A' <= char <= 'Z':
            base52_int = base52_int * 52 + (ord(char) - 65)
        elif 'a' <= char <= 'z':
            base52_int = base52_int * 52 + (ord(char) - 97 + 26)

    # Convert base-256 integer to string
    bytes_list = []
    while base52_int > 0:
        bytes_list.insert(0, base52_int % 256)
        # ^ extracts least significant byte (mod 256)
        # and puts it at the start of the array
        base52_int //= 256 # shift down a byte
    output_str = "".join(chr(byte) for byte in bytes_list)
    # ^ =
        #output_str = ""
        #for byte in byte_list:
        #	output_str += chr(byte)
    output_str2 = ""
    for byte in bytes_list:
        output_str2 += chr(byte)
    return output_str2

test = "wtf it actuall works"
testb52e = b52_encode(test)
print("Encoded:", testb52e)
testb52d = b52_decode(testb52e)
print("Decoded:", testb52d)
<<<<<<< HEAD
=======
=======
    
    # Convert base-256 integer to base26 string
    if base256_int == 0:
        return 'A'  # Special case for empty input or input that equals zero
    
    base26_str = ""
    while base256_int > 0:
        base26_str = chr(base256_int % 26 + 65) + base26_str
        base256_int //= 26
    
    return base26_str

def b26_decode(input_string):
    # Convert base26 string to a base-256 integer
    base26_int = 0
    for char in input_string:
        base26_int = base26_int * 26 + (ord(char) - 65)
    
    # Convert base-256 integer to string
    bytes_list = []
    while base26_int > 0:
        bytes_list.insert(0, base26_int % 256)
        base26_int //= 256
    
    return ''.join(chr(byte) for byte in bytes_list)
>>>>>>> master
>>>>>>> master
