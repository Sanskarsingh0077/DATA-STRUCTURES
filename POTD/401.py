class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        '''
        res = []

        for HH in range(12):
            for MM in range(60):
                if (HH.bit_count() + MM.bit_count()) == turnedOn:
                    hour = str(HH)
                    minutes = ("0" if MM < 10 else "") + str(MM)

                    res.append(hour + ":" + minutes)


        return res
        '''

        return [
            f"{h}:{m:02d}"
            for h in range(12)
            for m in range(60)
            if h.bit_count() + m.bit_count() == turnedOn

        ]