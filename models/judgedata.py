from models.judge import Judge,CreateActiveJudge
from plugins import db

class JudgeData
    def __init__(self,JudgeDataRecord,court_name,Termination_specific_reason):
        self.Judge_Identification_Number = JudgeDataRecord.Judge_Identification_Number
        self.Judge_Last_Name = JudgeDataRecord.Judge_Last_Name
        self.Judge_Middle_Name = JudgeDataRecord.Judge_Middle_Name
        self.Judge_First_Name = JudgeDataRecord.Judge_First_Name
        self.Suffix = JudgeDataRecord.Suffix
        self.Court_Name = court_name
        self.Termination_specific_reason = Termination_specific_reason

    def full_name(self):
        return self.Judge_First_Name + ' ' + self.Judge_Middle_Name + ' ' self.Judge_Last_Name + ' ' self.Suffix

    def __repr__(self):
        pass

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
        self.Termination_specific_reason_1  = row[45]
        self.Judge_Identification_Number_b = row[46]
        self.Court_Name_2 = row[47]
        self.Court_Type_2 = row[48]
        self.Termination_specific_reason_2  = row[74]
        self.Judge_Identification_Number_c = row[75]
        self.Court_Name_3 = row[76]
        self.Court_Type_3 = row[77]
        self.Termination_specific_reason_3  = row[103]
        self.Judge_Identification_Number_d = row[104]
        self.Court_Name_4 = row[105]
        self.Court_Type_4 = row[106]
        self.Termination_specific_reason_4  = row[132]
        self.Judge_Identification_Number_e = row[133]
        self.Court_Name_5 = row[134]
        self.Court_Type_5 = row[135]
        self.Termination_specific_reason_4  = row[161]
        self.Judge_Identification_Number_f = row[162]
        self.Court_Name_5 = row[163]
        self.Court_Type_5 = row[164]
        #self.Court_Name = ''


    @static
    def add_all_allowed_judges_to_database(judgedatarow_list):
        for judgedatarow in judgedatarow_list:
            Judge(judgedatarow).add_to_database_if_allowed()
        db.session.commit()

    #command executor: executes based on query result
    def add_to_database_if_allowed(self):
        judgedata = self.get_judge_to_add_to_database():
        if judgedata:
            add_judge_to_database(judgedata)

    #query
    #returns result based on internal state, does not change or effect internal state
    def get_judge_to_add_to_database(self):
        #in
        if len(self.Termination_specific_reason_1.trim()) == 0:
            return JudgeData(self,self.Court_Name_1,self.Termination_specific_reason_1.trim())
        #out
        if expired(self.Termination_specific_reason_1.trim()):
            return None
        #check next set of data
        #in
        if len(self.Termination_specific_reason_2.trim()) == 0:
            return JudgeData(self,self.Court_Name_2,self.Termination_specific_reason_2.trim())
        #out
        if expired(Termination_specific_reason_2.trim()):
            return None
        #check next set of data
        #in
        if len(self.Termination_specific_reason_3.trim()) == 0:
            return JudgeData(self,self.Court_Name_3,self.Termination_specific_reason_3.trim())
        #out
        if expired(Termination_specific_reason_3.trim()):
            return None

        #check next set of data
        #in
        if len(self.Termination_specific_reason_4.trim()) == 0:
            return JudgeData(self,self.Court_Name_4,self.Termination_specific_reason_4.trim())
        #out
        if expired(Termination_specific_reason_4.trim()):
            return None

        #check next set of data
        #in
        if len(self.Termination_specific_reason_5.trim()) == 0:
            return JudgeData(self,self.Court_Name_5,self.Termination_specific_reason_5.trim())
        #out
        if expired(Termination_specific_reason_5.trim()):
            return ""

        #check next set of data
        #in
        if len(self.Termination_specific_reason_6.trim()) == 0:
            return JudgeData(self,self.Court_Name_6,self.Termination_specific_reason_6.trim())
        #out
        if expired(Termination_specific_reason_6.trim()):
            return ""

    def expired(self,Termination_specific_reason):
        if Termination_specific_reason == "Retirement":
            return true
        if Termination_specific_reason == "Death":
            return true
        if Termination_specific_reason == "Resignation":
            return true
        if Termination_specific_reason == "Impeachment & Conviction":
            return true
        return false


    #command
    #changes backing data store, does not change or effect internal state
    @static
    def add_judge_to_database(self,judgedata):
        judge = CreateActiveJudge(name=judgedata.full_name,state="CA",court=judgedata.Court_Name, district="")
        #print judgedata
        #db.session.add(judge)






