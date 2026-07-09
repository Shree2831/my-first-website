class Node:
    def __init__(self, song_name):
        self.song_name = song_name
        self.next = None


class Playlist:
    def __init__(self):
        self.head = None

    def create_playlist(self, song_name):
        new_node = Node(song_name)

        if self.head is None:
            self.head = new_node
            return

        current = self.head
        while current.next:
            current = current.next

        current.next = new_node

    def insert_song(self, song_name):
        new_node = Node(song_name)
        new_node.next = self.head
        self.head = new_node

    def delete_song(self, song_name):
        if self.head is None:
            return

        if self.head.song_name == song_name:
            self.head = self.head.next
            return

        current = self.head
        while current.next:
            if current.next.song_name == song_name:
                current.next = current.next.next
                return
            current = current.next

    def search_song(self, song_name):
        current = self.head

        while current:
            if current.song_name == song_name:
                return True
            current = current.next

        return False

    def display_playlist(self):
        current = self.head

        while current:
            print(current.song_name, end=" -> ")
            current = current.next

        print("None")



playlist = Playlist()


playlist.create_playlist("Leo")
playlist.create_playlist("Vikram")
playlist.create_playlist("Master")

print("Playlist:")
playlist.display_playlist()


playlist.insert_song("Jailer")

print("\nAfter Insert:")
playlist.display_playlist()


playlist.delete_song("Vikram")

print("\nAfter Delete:")
playlist.display_playlist()


if playlist.search_song("Master"):
    print("\nSong Found")
else:
    print("\nSong Not Found")


