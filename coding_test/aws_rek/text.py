import boto3
import image_helpers
import os
import argparse

if __name__ == "__main__":

    #bucket='bucket'
    #photo='inputtext.jpg'

    client=boto3.client('rekognition',
        aws_access_key_id='AKIAIUEYJCZTJUIVTIXA',
        aws_secret_access_key='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',
        region_name='us-east-1')


    #imgurl = 'https://australianfintech.com.au/wp-content/uploads/2018/05/Advice.jpeg'
    #imgurl = 'https://i.imgur.com/1FwHQja.png'
    #filename = '/home/jf/Downloads/invoice-test/invoice4.png'

    parser = argparse.ArgumentParser(description='Recive a Path of a Folder')
    parser.add_argument('directory', type=str, help='A folder path')

    args = parser.parse_args()
    folder = args.directory

    filenames = os.listdir(folder)
    #imgbytes = image_helpers.get_image_from_url(imgurl)
    imgbytes = image_helpers.get_image_from_file(folder + filenames[3])

    #response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    response=client.detect_text(Image={'Bytes': imgbytes})

    textDetections=response['TextDetections']
    print(response)
    print('Matching faces')
    for text in textDetections:
            print('Detected text:' + text['DetectedText'])
            print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
            print('Id: {}'.format(text['Id']))
            if 'ParentId' in text:
                print('Parent Id: {}'.format(text['ParentId']))
            print('Type:' + text['Type'])
            print('\n')
