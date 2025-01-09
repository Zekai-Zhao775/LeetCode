class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        result = []

        # nums of rows
        m = len(matrix)
        # nums of columns
        n = len(matrix[0])

        num_of_elements = m * n

        m_current = 0
        n_current = 0

        m_border_up = 1
        m_border_down = m - 1

        n_border_left = 0
        n_border_right = n - 1

        direction = 'right'

        while len(result) != num_of_elements - 1:
            if direction == 'right':
                if n_current < n_border_right:
                    result.append(matrix[m_current][n_current])
                    n_current += 1
                elif n_current == n_border_right:
                    n_border_right -= 1
                    direction = "down"

            elif direction == "down":
                if m_current < m_border_down:
                    result.append(matrix[m_current][n_current])
                    m_current += 1
                elif m_current == m_border_down:
                    m_border_down -= 1
                    direction = "left"

            elif direction == "left":
                if n_current > n_border_left:
                    result.append(matrix[m_current][n_current])
                    n_current -= 1
                elif n_current == n_border_left:
                    n_border_left += 1
                    direction = "up"

            elif direction == "up":
                if m_current > m_border_up:
                    result.append(matrix[m_current][n_current])
                    m_current -= 1
                elif m_current == m_border_up:
                    m_border_up += 1
                    direction = "right"

        result.append(matrix[m_current][n_current])
        return result