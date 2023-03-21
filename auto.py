import fitz

filename = "foo"

doc = fitz.open(f"raw/{filename}.pdf")
out = fitz.open()
out.insert_pdf(doc, from_page = 0)
for p in range(out.page_count):
    xref = out[p].get_contents()[0]
    cont = bytearray(out.xref_stream(xref))
    # print(cont.count(b"re"))
    end = True
    idx = 0
    D = []
    while end:
        ed = cont.find(b"re",idx)
        st = cont.rfind(b"\n",0,ed)
        idx = ed+1
        if ed == -1:
            end = False
            break
        D.append(cont[st+2:ed+3])
        # print(i, cont[st+2:ed+4])
        # print(cont[st+3:ed-1].split(b" ")[2])
    
    for d in D:
        # print(i,d)
        # print(float(d[1:].split(b" ")[2]))
        w = float(d[1:].split(b" ")[2])
        if d[1:].split(b" ")[3] == b"re\n":
            continue
        h = float(d[1:].split(b" ")[3])
        if w > 200 and w < 840 and h > 30:
            print(f"{p}, ",end="")
            cont = cont.replace(d, b"")
    out.update_stream(xref, cont)
out.save(f"out/{filename}.pdf")
