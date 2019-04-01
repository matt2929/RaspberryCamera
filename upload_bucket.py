import boto3

def upload_newest_pic():
	s3 = boto3.client('s3')

	response = s3.list_buckets()

	print(response)

	buckets = response['Buckets']

	buckets = [bucket['Name'] for bucket in response['Buckets']]

	if "mattsraspi" in buckets:
		print("ladies and gentleman we gotem")
		filename = '/home/pi/Desktop/security/pic_recent.jpeg'
		bucket_name = 'mattsraspi'
		s3.upload_file(filename, bucket_name, 'pics/pic_recent.jpg')
