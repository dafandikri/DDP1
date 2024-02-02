import unittest
import tp4

barcode = tp4.Barcode()

class TestTp4(unittest.TestCase):
    # Testing checksum
    def test_checksum(self):
        self.assertEqual(barcode.checksum('123456789012'), '8')  # Testing
        self.assertEqual(barcode.checksum('899276113901'), '8')  # Ades
        self.assertEqual(barcode.checksum('899600160037'), '5')  # Le Minerale
        self.assertEqual(barcode.checksum('888501502159'), '0')  # Irvins Salted Egg
        self.assertEqual(barcode.checksum('880104810102'), '3')  # Jinro Soju
        self.assertEqual(barcode.checksum('888501652033'), '7')  # Clover Honey


    # Testing calculate_barcode (Structure, Checksum, and Country(BONUS))
    def test_calculate_barcode(self):
        self.assertEqual(barcode.calculate_barcode('123456789012'), ('1', 'LLGLGG', '234567890128', "USA and Canada"))  # Testing
        self.assertEqual(barcode.calculate_barcode('899276113901'), ('8', 'LGLGGL', '992761139018', "Indonesia"))  # Ades
        self.assertEqual(barcode.calculate_barcode('899600160037'), ('8', 'LGLGGL', '996001600375', "Indonesia"))  # Le Minerale
        self.assertEqual(barcode.calculate_barcode('888501502159'), ('8', 'LGLGGL', '885015021590', "Singapore"))  # Irvins Salted Egg
        self.assertEqual(barcode.calculate_barcode('880104810102'), ('8', 'LGLGGL', '801048101023', "South Korea"))  # Jinro Soju
        self.assertEqual(barcode.calculate_barcode('888501652033'), ('8', 'LGLGGL', '885016520337', "Singapore"))  # Clover Honey



    # Testing encode_digit_L, encode_digit_R, and encode_digit_G
    def test_encode_digit_L(self):
        self.assertEqual(barcode.encode_digit_L('0'), '0001101') 
        self.assertEqual(barcode.encode_digit_L('1'), '0011001')
        self.assertEqual(barcode.encode_digit_L('2'), '0010011')
        self.assertEqual(barcode.encode_digit_L('3'), '0111101')
        self.assertEqual(barcode.encode_digit_L('4'), '0100011')
        self.assertEqual(barcode.encode_digit_L('5'), '0110001')
        self.assertEqual(barcode.encode_digit_L('6'), '0101111')
        self.assertEqual(barcode.encode_digit_L('7'), '0111011')
        self.assertEqual(barcode.encode_digit_L('8'), '0110111')
        self.assertEqual(barcode.encode_digit_L('9'), '0001011')

    def test_encode_digit_R(self):
        self.assertEqual(barcode.encode_digit_R('0'), '1110010')
        self.assertEqual(barcode.encode_digit_R('1'), '1100110')
        self.assertEqual(barcode.encode_digit_R('2'), '1101100')
        self.assertEqual(barcode.encode_digit_R('3'), '1000010')
        self.assertEqual(barcode.encode_digit_R('4'), '1011100')
        self.assertEqual(barcode.encode_digit_R('5'), '1001110')
        self.assertEqual(barcode.encode_digit_R('6'), '1010000')
        self.assertEqual(barcode.encode_digit_R('7'), '1000100')
        self.assertEqual(barcode.encode_digit_R('8'), '1001000')
        self.assertEqual(barcode.encode_digit_R('9'), '1110100')

    def test_encode_digit_G(self):
        self.assertEqual(barcode.encode_digit_G('0'), '0100111')
        self.assertEqual(barcode.encode_digit_G('1'), '0110011')
        self.assertEqual(barcode.encode_digit_G('2'), '0011011')
        self.assertEqual(barcode.encode_digit_G('3'), '0100001')
        self.assertEqual(barcode.encode_digit_G('4'), '0011101')
        self.assertEqual(barcode.encode_digit_G('5'), '0111001')
        self.assertEqual(barcode.encode_digit_G('6'), '0000101')
        self.assertEqual(barcode.encode_digit_G('7'), '0010001')
        self.assertEqual(barcode.encode_digit_G('8'), '0001001')
        self.assertEqual(barcode.encode_digit_G('9'), '0010111')

if __name__ == '__main__':
    unittest.main()