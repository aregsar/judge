import csv
from models.judge import Judge,CreateActiveJudge
from plugins import db

class JudgeData:
    def __init__(self,JudgeDataRecord,court_name,Termination_specific_reason):
        self.Judge_Identification_Number = JudgeDataRecord.Judge_Identification_Number
        self.Judge_Last_Name = JudgeDataRecord.Judge_Last_Name
        self.Judge_Middle_Name = JudgeDataRecord.Judge_Middle_Name
        self.Judge_First_Name = JudgeDataRecord.Judge_First_Name
        self.Suffix = JudgeDataRecord.Suffix
        self.Court_Name = court_name
        self.Termination_specific_reason = Termination_specific_reason


    def full_name(self):
        return self.Judge_First_Name + ' ' + self.Judge_Middle_Name + ' ' + self.Judge_Last_Name + ' ' + self.Suffix

    def __repr__(self):
        return '<judge id={id}  \
            ,last={last}  \
            ,middle={middle}  \
            ,first={first}  \
            ,suffix={suffix}  \
            ,court={court}  \
            ,term={term}  \
            >'.format(id=self.Judge_Identification_Number,
            last=self.Judge_Last_Name,
            middle=self.Judge_First_Name,
            first=self.Judge_Middle_Name,
            suffix=self.Suffix,
            court=self.Court_Name,
            term=self.Termination_specific_reason)



class JudgeDataRecord():

    """
Termination specific reason <values: (Empty)=>add judge and court name as sitting judge,
[Retirement]=>add as retired judge without court name (for now dont add),
[Death, Resignation,Impeachment & Conviction ]=>remove from list ,
[Reassignment, Appointment to Another Judicial Position, Recess Appointment-Not Confirmed] => defer to next pass
>
    """
    def __init__(self,row):
        self.Judge_Identification_Number = row[0]
        self.Judge_Last_Name = row[1]
        self.Judge_Middle_Name = row[2]
        self.Judge_First_Name = row[3]
        self.Suffix = row[4]
        self.Judge_Identification_Number_a = row[17]
        self.Court_Name_1 = row[18]
        self.Court_Type_1 = row[19]
        self.Termination_specific_reason_1  = row[46]
        self.Judge_Identification_Number_b = row[47]
        self.Court_Name_2 = row[48]
        self.Court_Type_2 = row[49]
        self.Termination_specific_reason_2  = row[75]
        self.Judge_Identification_Number_c = row[76]
        self.Court_Name_3 = row[77]
        self.Court_Type_3 = row[78]
        self.Termination_specific_reason_3  = row[104]
        self.Judge_Identification_Number_d = row[105]
        self.Court_Name_4 = row[106]
        self.Court_Type_4 = row[107]
        self.Termination_specific_reason_4  = row[133]
        self.Judge_Identification_Number_e = row[134]
        self.Court_Name_5 = row[135]
        self.Court_Type_5 = row[136]
        self.Termination_specific_reason_5  = row[162]
        self.Judge_Identification_Number_f = row[163]
        self.Court_Name_6 = row[164]
        self.Court_Type_6 = row[165]
        #self.Court_Name = ''

    def __repr__(self):
        return '<id={id}  \
            ,ida={ida}  \
            ,idb={idb}  \
            ,idc={idc}  \
            ,idd={idd}  \
            ,ide={ide}  \
            ,idf={idf}  \
            ,last={last}  \
            ,middle={middle}  \
            ,first={first}  \
            ,suffix={suffix}  \
            ,court1={court1}  \
            ,type1={type1}  \
            ,term1={term1}  \
            ,court2={court2}  \
            ,type2={type2}  \
            ,term2={term2}  \
            ,court3={court3}  \
            ,type3={type3}  \
            ,term3={term3}  \
            ,court4={court4}  \
            ,type4={type4}  \
            ,term4={term4}  \
            ,court5={court5}  \
            ,type5={type5}  \
            ,term5={term5}  \
            ,court6={court6}  \
            ,type6={type6}>'.format(id=self.Judge_Identification_Number,
            ida=self.Judge_Identification_Number_a,
            idb=self.Judge_Identification_Number_b,
            idc=self.Judge_Identification_Number_c,
            idd=self.Judge_Identification_Number_d,
            ide=self.Judge_Identification_Number_e,
            idf=self.Judge_Identification_Number_f,
            last=self.Judge_Last_Name,
            middle=self.Judge_First_Name,
            first=self.Judge_Middle_Name,
            suffix=self.Suffix,
            court1=self.Court_Name_1,
            type1=self.Court_Type_1,
            term1=self.Termination_specific_reason_1,
            court2=self.Court_Name_2,
            type2=self.Court_Type_2,
            term2=self.Termination_specific_reason_2,
            court3=self.Court_Name_3,
            type3=self.Court_Type_3,
            term3=self.Termination_specific_reason_3,
            court4=self.Court_Name_4,
            type4=self.Court_Type_4,
            term4=self.Termination_specific_reason_4,
            court5=self.Court_Name_5,
            type5=self.Court_Type_5,
            term5=self.Termination_specific_reason_5,
            court6=self.Court_Name_6,
            type6=self.Court_Type_6)

    @staticmethod
    def load_file_data(filepath):
        with open(filepath,'rb') as file:
            contents = csv.reader(file)
            matrix = list()
            for row in contents:
                matrix.append(row)

        matrix.pop(0)#remove header row
        JudgeDataRecord.add_all_allowed_judges_to_database(matrix)

    @staticmethod
    def add_all_allowed_judges_to_database(judgedatarow_list):
        index=0
        judges=0
        for judgedatarow in judgedatarow_list:
            record = JudgeDataRecord(judgedatarow)
            # if index > 2000:
            #     print record
            #     record.add_to_database_if_allowed()
            #     break
            index += 1
            if record.add_to_database_if_allowed():
                judges += 1
            if judges > 200:
                break
        print str(index) + " total records"
        print str(judges) + " active judges"
        db.session.commit()
#########################################################################################
    #command executor: executes based on query result
    def add_to_database_if_allowed(self):
        judgedata = self.create_judgedata_to_add_to_database()
        if judgedata:
            #print judgedata
            JudgeDataRecord.add_judge_to_database(judgedata)
            return True
        return False
    #query
    #returns result based on internal state, does not change or effect internal state
    def create_judgedata_to_add_to_database(self):
        #in
        if len(self.Termination_specific_reason_1.strip()) == 0:
            return JudgeData(self,self.Court_Name_1,self.Termination_specific_reason_1.strip())
        #out
        if self.expired(self.Termination_specific_reason_1):
            return None
        #check next set of data
        #in
        if len(self.Termination_specific_reason_2.strip()) == 0:
            return JudgeData(self,self.Court_Name_2,self.Termination_specific_reason_2.strip())
        #out
        if self.expired(self.Termination_specific_reason_2.strip()):
            return None
        #check next set of data
        #in
        if len(self.Termination_specific_reason_3.strip()) == 0:
            return JudgeData(self,self.Court_Name_3,self.Termination_specific_reason_3.strip())
        #out
        if self.expired(self.Termination_specific_reason_3.strip()):
            return None

        #check next set of data
        #in
        if len(self.Termination_specific_reason_4.strip()) == 0:
            return JudgeData(self,self.Court_Name_4,self.Termination_specific_reason_4.strip())
        #out
        if self.expired(self.Termination_specific_reason_4.strip()):
            return None

        #check next set of data
        #in
        if len(self.Termination_specific_reason_5.strip()) == 0:
            return JudgeData(self,self.Court_Name_5,self.Termination_specific_reason_5.strip())
        #out
        if self.expired(self.Termination_specific_reason_5.strip()):
            return ""

        #check next set of data
        #in
        if len(self.Termination_specific_reason_6.strip()) == 0:
            return JudgeData(self,self.Court_Name_6,self.Termination_specific_reason_6.strip())
        #out
        if self.expired(Termination_specific_reason_6.strip()):
            return ""

    def expired(self,Termination_specific_reason):
        Termination_specific_reason = Termination_specific_reason.strip()
        if Termination_specific_reason == "Retirement":
            return True
        if Termination_specific_reason == "Death":
            return True
        if Termination_specific_reason == "Resignation":
            return True
        if Termination_specific_reason == "Impeachment & Conviction":
            return True
        return False


    #command
    #changes backing data store, does not change or effect internal state
    @staticmethod
    def add_judge_to_database(judgedata):
        judge = CreateActiveJudge(name=judgedata.full_name().strip(),state="CA",court=judgedata.Court_Name, district="")
        print judge
        db.session.add(judge)






