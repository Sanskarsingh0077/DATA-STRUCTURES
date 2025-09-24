def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        
        if numerator == 0:
            return "0"
        
        result = ""
        if numerator * denominator < 0:
            result += "-"
        
        absNumerator = abs(numerator)
        absDenominator= abs(denominator)

        intDivision = absNumerator//absDenominator

        result += str(intDivision)

        remain = absNumerator % absDenominator
        if remain == 0:
            return result

        else:
            result += "."

        mp = {}
        while remain:

            if remain in mp:
                    
                # insert "(" at the stored position
                idx = mp[remain]
                result = result[:idx] + "(" + result[idx:]  # O(length)
                result += ")"
                break

            mp[remain] = len(result)

            remain *= 10
            digit = remain // absDenominator
            result += str(digit)  # O(1)

            remain %= absDenominator


        return result