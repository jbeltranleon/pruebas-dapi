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
    #imgbytes = image_helpers.get_image_from_url(imgurl)
    #filename = '/home/jf/Downloads/invoice-test/invoice4.png'

    parser = argparse.ArgumentParser(description='Recive a Path of a Folder')
    parser.add_argument('directory', type=str, help='A folder path')

    args = parser.parse_args()
    folder = args.directory

    filenames = os.listdir(folder)
    print(filenames[0])

    for filename in filenames:
        list_imgbytes = []
        list_imgbytes.append(image_helpers.get_image_from_file(folder + filename))
    print('111111111111')
    print(len(list_imgbytes))

    #response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    for imgbytes in list_imgbytes:
        list_response = []
        list_response.append(client.detect_text(Image={'Bytes': imgbytes}))


    for response in list_response:
        list_textDetections=[]
        list_textDetections.append(response['TextDetections'])
        print(response)

    print('Matching')
    for textDetections in list_textDetections:
        print('***********************************************')
        print('***********************************************')
        for text in textDetections:
                print('Detected text:' + text['DetectedText'])
                print('Confidence: ' + "{:.2f}".format(text['Confidence']) + "%")
                print('Id: {}'.format(text['Id']))
                if 'ParentId' in text:
                    print('Parent Id: {}'.format(text['ParentId']))
                print('Type:' + text['Type'])
                print('\n')


    print('Correct format path example: /home/jf/Downloads/invoice-test/ ')
