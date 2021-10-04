# https://leetcode.com/problems/text-justification/

class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        total = []
        tmp = []
        current_size = 0
        for word in words:
            word_size = len(word)
            num_word = len(tmp)

            current_line_size = current_size + num_word

            if current_line_size + word_size > maxWidth:
                total.append(tmp)
                tmp = []
                current_size = 0

            tmp.append(word)
            current_size += word_size

        if tmp:
            total.append(tmp)

        # return total
        final = []
        num_line = len(total)
        for lind_idx, pack in enumerate(total):
            num_word = len(pack)
            current_length = sum(map(len, pack))

            space_size = maxWidth - current_length
            space_place = num_word - 1

            if lind_idx == num_line - 1:
                last_line = " ".join(pack) if num_word > 1 else pack[0]
                final_str = last_line + " " * (space_size - (num_word - 1))
            elif space_place > 0:
                base, rest = divmod(space_size, space_place)
                space_lengths = [
                    (base + 1) if i < rest else base
                    for i in range(space_place)
                ]

                final_str = pack[0]
                for i in range(space_place):
                    space = space_lengths[i]
                    word = pack[i + 1]
                    final_str += " " * space
                    final_str += word
            else:
                final_str = pack[0] + " " * space_size

            final.append(final_str)


        return final
