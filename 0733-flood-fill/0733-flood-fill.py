from collections import deque

class Solution:

    def get_neighbours(self, sr: int, sc:int):
        neighbours = []
        for i,j in [(0,-1), (0,1), (-1,0), (1,0)]:
            r, c = sr + i, sc + j
            if 0 <= r < len(self.image) and 0 <= c < len(self.image[0]):
                neighbours.append((r,c))
        return neighbours

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        self.image = image
        color_org = image[sr][sc]
        queue = deque([(sr, sc)])
        visited = set()
        
        while len(queue) > 0:
            current_coord = queue.popleft()
            if current_coord in visited:
                continue

            r,c = current_coord
            image[r][c] = color

            for neighbour in self.get_neighbours(r,c):
                r,c = neighbour
                color_here = image[r][c]
                
                if color_here == color_org:
                    queue.append(neighbour)
            visited.add(current_coord)

        return image
