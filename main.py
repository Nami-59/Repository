from function import read_data

def main():
    data = read_data("text.txt")
    for line in data:
        print(line.strip())

if __name__ == "__main__":
    main()