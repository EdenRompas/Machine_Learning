# netlify-functions/my_function.py
def handler(event, context):
    # Kode fungsi Anda di sini
    return {
        'statusCode': 200,
        'body': 'Hello from Netlify Function!'
    }
