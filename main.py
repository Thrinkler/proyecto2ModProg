import cli

def main():
    parser = cli.start_parser()
    args = parser.parse_args()
    print(args)
    
    pass

if __name__ == "__main__":
    main()
    
