def get_image():
    from PIL import Image, ImageDraw

    def draw_square(pillow_image_draw: ImageDraw.Draw, cord_position: tuple, color_code: str):
        pillow_image_draw.rectangle(cord_position, fill=color_code)

    def execute_command_on_image(image: Image, command_list: list[list]):
        color_codes = {0: "red", 1: "green", 2: "blue"}
        pillow_image_draw = ImageDraw.Draw(image)
        for rectangle_type_index in range(len(command_list)):
            for rectangle_cords in command_list[rectangle_type_index]:
                draw_square(pillow_image_draw, rectangle_cords, color_codes[rectangle_type_index])

    def process_string_command(command_text: str) -> list[list]:
        source_command_list = [[], [], []]

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

    def main():
        X_IMAGE_SIZE = 512
        Y_IMAGE_SIZE = 512

        COLOR_CODE = "RGB"

        BACKGROUND_COLOR = (255, 255, 255)

        commands_list = process_string_command(command_text=input())
        image = Image.new(COLOR_CODE, (X_IMAGE_SIZE, Y_IMAGE_SIZE), BACKGROUND_COLOR)
        execute_command_on_image(image, commands_list)
        image.show()
        print(commands_list)    

    #starting the program
    main()

get_image()