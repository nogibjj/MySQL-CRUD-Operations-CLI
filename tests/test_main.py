import subprocess


def test_main():
    """
    This functions tests
    our main function"""
    # Run the script with the flag
    result = subprocess.run(["python", "main.py", "--query"], stdout=subprocess.PIPE)
    output = result.stdout.decode("utf-8")
    with open("output.txt", "w") as f:
        f.write(output)

    # Add, commit, and push the file to your GitHub repository
    subprocess.run(["git", "add", "output.txt"])
    subprocess.run(["git", "commit", "-m", "Added output.txt"])
    subprocess.run(["git", "push"])


if __name__ == "__main__":
    test_main()
