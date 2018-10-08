import boto3
import image_helpers
import os
import argparse
import json

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
    print(filenames)

    list_imgbytes = []
    for filename in filenames:
        list_imgbytes.append(image_helpers.get_image_from_file(folder + filename))

    #response=client.detect_text(Image={'S3Object':{'Bucket':bucket,'Name':photo}})
    list_response = []
    for imgbytes in list_imgbytes:
        list_response.append(client.detect_text(Image={'Bytes': imgbytes}))

    #Json file
    # with open('data.json', mode='w', encoding='utf-8') as f:
    #     json.dump([], f)

    list_textDetections=[]
    for response in list_response:
        list_textDetections.append(response['TextDetections'])
        print(response)
        with open('data.json', 'a') as outfile:
            json.dump(response, outfile, sort_keys = True, indent = 4,
               ensure_ascii = False)
        # with open('data.json', mode='w', encoding='utf-8') as feedsjson:
        #     feeds.append(response)
        #     json.dump(feeds, feedsjson)

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
