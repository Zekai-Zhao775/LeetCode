from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        i = len(asteroids) - 1
        while i >= 0:
            if i < len(asteroids) - 1:
                if asteroids[i] > 0:
                    if asteroids[i] + asteroids[i + 1] > 0 and asteroids[i + 1] < 0:
                        asteroids.pop(i + 1)
                    elif asteroids[i] + asteroids[i + 1] == 0:
                        asteroids.pop(i + 1)
                        asteroids.pop(i)
                    elif asteroids[i] + asteroids[i + 1] < 0:
                        asteroids.pop(i)
                    else:
                        i -= 1
                else:
                    i -= 1
            else:
                i -= 1

        return asteroids