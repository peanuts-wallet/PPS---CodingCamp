class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_list = list(s)
        t_list = list(t)

        for i in range(len(s_list)):
            if s_list[i] == '#':
                s_list[i] = ""
                for j in range(i - 1, -1, -1):
                    if s_list[j] != "":
                        s_list[j] = ""
                        break

        for i in range(len(t_list)):
            if t_list[i] == '#':
                t_list[i] = ""
                for j in range(i - 1, -1, -1):
                    if t_list[j] != "":
                        t_list[j] = ""
                        break
        return "".join(s_list) == "".join(t_list)