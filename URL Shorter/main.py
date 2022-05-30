def finder(url):
    find = url.find("https://")

    if find == -1:
        if url.count("www.") == 1:
            url = url[4:]

        else:
            pass

    else:
        url = url[find + 8:]

        if url.count("www.") == 1:
            url = url[4:]

        else:
            pass

    dot = url.find(".")

    if url.find(".") == -1:
        return f"Your website's name is: {url}"

    else:
        return f"Your website's name is: {url[:dot]}"

def main():
    url = input("Enter your WEB Site: ")
    print(finder(url))

if __name__ == '__main__':
    main()