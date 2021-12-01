def get_image():
    from PIL import Image, ImageDraw
    '''
    Function which drawing rectangle with fixed width and height
    args: DrawImage Pillow's object for drawing, tuple with positions of left top and bottom right cords, name of rectangle's color
    response: None (cause again all changes automatically will be saved in DrawImage object example) 
    '''
    def draw_square(pillow_image_draw: ImageDraw.Draw, cord_position: tuple, color_code: str):
        pillow_image_draw.rectangle(cord_position, fill=color_code)

    '''
    Function for creating ImageDraw object for finally draw rectangles
    args: link for created image object by Pillow library, list of commands
    response: None (cause all changes automatically will be processed on original object)
    '''
    def execute_command_on_image(image: Image, command_list: list[list]):
        #list which contains names of three colors
        color_codes =["red", "green", "blue"]
        #rectangle side length in pixels for find postion of bottom right rectangle's point
        rectangle_side_length = 50

        # creating ImageDraw object
        pillow_image_draw = ImageDraw.Draw(image)
        for rectangle_type_index in range(len(command_list)):
            for rectangle_cords in command_list[rectangle_type_index]:
                draw_square(pillow_image_draw, 
                            (rectangle_cords[0], rectangle_cords[1],
                             rectangle_cords[0] + rectangle_side_length, rectangle_cords[1] + rectangle_side_length),
                            color_codes[rectangle_type_index])
    '''
    Function, where by eval function i converting string into list of executable commands
    args: text message from input 
    response: list, which contains another 3 list (each one for each color), which  is contains lists with cords of rectagles
    '''
    def get_processed_string_command(command_text: str) -> list[list]:
        source_command_list = [[], [], []]

        '''
        Function for one fast check for validation of command
        args: commands list
        response: boolean result of check
        '''
        def check_valid_command(command_list: list[list]) -> bool:
            return type(command_list) == list and\
                   len(command_list) == len(source_command_list) and\
                   all([type(section) == list for section in command_list])
        
        try:
            command_list_for_check = eval(command_text)
            if check_valid_command(command_list_for_check):
                return command_list_for_check
            else:
                raise NameError("Invalid command")
        except NameError:
            pass
                
        return source_command_list     

    def main() -> Image:
        #constants serialization
        X_IMAGE_SIZE = 512
        Y_IMAGE_SIZE = 512

        COLOR_CODE = "RGB"

        BACKGROUND_COLOR = (0, 0, 0)

        #getting list of commands by input
        commands_list = get_processed_string_command(command_text=input())
        #creating image
        main_image = Image.new(COLOR_CODE, (X_IMAGE_SIZE, Y_IMAGE_SIZE), BACKGROUND_COLOR)
        execute_command_on_image(main_image, commands_list)
        #returning final image
        return main_image 

    #starting the program
    return main()

get_image()