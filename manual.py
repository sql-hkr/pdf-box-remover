import fitz

filename = "foo"
# e.g. info = [[10,8],[11,2],[12,4],[13,4]]
info = []

doc = fitz.open(f"raw/{filename}.pdf")
out = fitz.open()
out.insert_pdf(doc, from_page = 0)
for i in info:
    xref = out[i[0]].get_contents()[0]
    cont = bytearray(out.xref_stream(xref))
    cont = cont[::-1].replace(b"re"[::-1], b"",i[1])[::-1]
    out.update_stream(xref, cont)
out.save(f"out/{filename}.pdf")
