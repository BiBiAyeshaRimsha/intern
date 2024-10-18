def hamming_encode(data):
    """
    Encode a 4-bit data string using Hamming code (7,4).
    """
    if len(data) != 4 or not all(bit in '01' for bit in data):
        raise ValueError("Input must be a 4-bit binary string.")

    # Initialize the codeword with placeholders for parity bits
    codeword = ['0'] * 7

    # Assign data bits to their positions
    codeword[2] = data[0]  # Position 3
    codeword[4] = data[1]  # Position 5
    codeword[5] = data[2]  # Position 6
    codeword[6] = data[3]  # Position 7

    # Calculate parity bits
    parity_positions = [0, 1, 3]  # Positions 1, 2, 4
    for pos in parity_positions:
        parity = 0
        for i in range(7):
            if (i + 1) & (pos + 1):
                parity ^= int(codeword[i])
        codeword[pos] = str(parity)

    return ''.join(codeword)

def hamming_decode(codeword):
    """
    Decode a 7-bit Hamming codeword, correcting single-bit errors.
    """
    if len(codeword) != 7 or not all(bit in '01' for bit in codeword):
        raise ValueError("Input must be a 7-bit binary string.")

    # Calculate parity checks
    parity_positions = [0, 1, 3]  # Positions 1, 2, 4
    error_pos = 0
    for pos in parity_positions:
        parity = 0
        for i in range(7):
            if (i + 1) & (pos + 1):
                parity ^= int(codeword[i])
        if parity != int(codeword[pos]):
            error_pos += pos + 1

    # Correct the error if detected
    if error_pos:
        error_pos -= 1  # Adjust to zero-based index
        corrected = list(codeword)
        corrected[error_pos] = '1' if codeword[error_pos] == '0' else '0'
        codeword = ''.join(corrected)

    # Extract data bits
    data_bits = [codeword[2], codeword[4], codeword[5], codeword[6]]
    return ''.join(data_bits)

# Example usage:
data = "1011"
encoded = hamming_encode(data)
print(f"Encoded: {encoded}")
received = "1110010"  # Example with an error in position 2
decoded = hamming_decode(received)
print(f"Decoded: {decoded}")
