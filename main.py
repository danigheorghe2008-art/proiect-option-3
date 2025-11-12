from models import Category, Expense
from repository import Repository
from service import service
from menu import run_menu


def main():
    repo = Repository()
    app_service = service(repo, Category, Expense)
    run_menu(app_service)


if __name__ == "__main__":
    main()
