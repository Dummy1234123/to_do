def main():
    with open("to_do.txt", "r") as file:
        to_do = [line.strip() for line in file]

    while True:
        print("\nYour to-do list:")
        for index, task in enumerate(to_do):
            print(f"{index}: {task}")

        ans = input("Enter index of completed task or 'q' to quit: ").strip()

        if ans.lower() == "q":
            break

        if ans.isdigit():
            index = int(ans)
            if 0 <= index < len(to_do):
                completed = to_do.pop(index)
                print(f"Removed: {completed}")
            else:
                print("Error: Index is too large.")
        else:
            print("Error: Please enter a valid number or 'q'.")

    # Write updated tasks back to file
    with open("to_do.txt", "w") as file:
        for task in to_do:
            file.write(task + "\n")
    return
