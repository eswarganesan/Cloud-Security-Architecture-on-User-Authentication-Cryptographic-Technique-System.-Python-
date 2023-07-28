if os.path.exists(
        "G:/ESWAR/INTERN/Edge Computing/Decryption/{0}".format(filename)):
    with open("G:/ESWAR/INTERN/Edge Computing/Decryption/{0}".format(filename),
              'rb') as fh:
        print(fh.read())
        response = HttpResponse(fh.read(), content_type="application/vnd.ms-excel")
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(
            ("G:/ESWAR/INTERN/Edge Computing/Decryption/{0}".format(filename)))
        return response
raise Http404