class Note:
    def __init__(self, content):
        self.content = content

class Notebook:
    def __init__(self, title):
        self.title = title
        self.pages = []

    def create_page(self, content):
        if len(self.pages) >= 300:
            print("더 이상 페이지를 추가할 수 없습니다.")
            return

        note = Note(content)
        self.pages.append(note)
        print("페이지가 추가되었습니다.")

    def delete_page(self, index):
        if index < 0 or index >= len(self.pages):
            print("유효하지 않은 페이지 인덱스입니다.")
            return

        del self.pages[index]
        print("페이지가 삭제되었습니다.")

    def change_page_content(self, index, new_content):
        if index < 0 or index >= len(self.pages):
            print("유효하지 않은 페이지 인덱스입니다.")
            return

        self.pages[index].content = new_content
        print("페이지 내용이 변경되었습니다.")

    def display_all_pages(self):
        print(f"전체 페이지 수: {len(self.pages)}")
        for i, page in enumerate(self.pages):
            print(f"페이지 {i+1}: {page.content}")


# 노트북 생성
notebook = Notebook("My Notebook")

# 3개의 페이지 생성
notebook.create_page("You made me feel so high")
notebook.create_page("Then crashed me to the ground")
notebook.create_page("Every time that I cry")

# 총 페이지 수 출력
notebook.display_all_pages()

# 새로운 페이지 추가
notebook.create_page("My tears don't ever dry")

# 총 페이지 수 출력
notebook.display_all_pages()

# 한 페이지 삭제
notebook.delete_page(2)

# 총 페이지 수 출력
notebook.display_all_pages()

# 특정 페이지 내용 변경
notebook.change_page_content(1, "Know I messed up this time")

# 전체 페이지 내용 출력
notebook.display_all_pages()