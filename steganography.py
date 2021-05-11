import sys
import datetime
from stegano import lsb

# encrypts message in images

if __name__ == "__main__":
	args = sys.argv
	assert len(args) > 1

	img_path = sys.argv[1]
	date = datetime.datetime.now()
	secret_msg = f"Copyright {date.year} Satya Borgohain"

	secret = lsb.hide(img_path, secret_msg)
	secret.save(f"{img_path}_encoded.jpg")
	print("==> Text successfully encoded.")
	decoded_msg = lsb.reveal(f"{img_path}_encoded.jpg")
	print(f"==> Text successfully decoded: {decoded_msg}")