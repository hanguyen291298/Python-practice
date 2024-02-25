HOLDER_NAME = "[name]"
with open(r".\Input\Names\invited_names.txt") as name_file:
    for name in name_file:
        new_name = name.strip()
        with open(r".\Input\Letters\starting_letter.txt") as file:
            data = file.readlines()
            for line in data:
                new_line = line.replace(HOLDER_NAME, new_name)
                with open(f"letter_for_{new_name}.txt", "a") as new_file:
                    new_file.write(new_line)






