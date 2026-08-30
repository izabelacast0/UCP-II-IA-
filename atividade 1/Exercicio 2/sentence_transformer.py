from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer("all-MiniLM-L6-v2")

code1 = "public boolean canEnroll(Student student) {return student.isActive() && student.getCompletedCredits() >= 120;}"
code2 = "public boolean canGraduate(Student student) {if (student.isActive() && student.getCompletedCredits() >= 120) {return true;}return false;}}"

emb1 = model.encode(code1)
emb2 = model.encode(code2)

similarity = util.cos_sim(emb1, emb2)

print(similarity)