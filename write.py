def main():
    with open("to_do.txt", "a") as file:
        while True:
            do_add_task = input("Do you want to add a task (y/n): ").strip().lower()
            if do_add_task == "y":
                task = input("What task do you want to add? ")
                file.write(f"{task}\n")
            elif do_add_task == "n":
                break
            else:
                print("Error: Please enter 'y' or 'n'.")


