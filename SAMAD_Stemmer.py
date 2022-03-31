
# Algorithm: Mohcine Maghfour, Abdeljalil Elouardighi (2022)
# Author: Mohcine Maghfour <maghfour.mohcin@gmail.com>


class Samad:
    """
SAMAD stemmer - Standard Arabic and Moroccan Arabic Dialect Stemmer - : 
is a light Arabic stemmer that removes the common prefixes and 
suffixes from Arabic words. Besides the stemming of standard Arabic, 
SAMAD stemmer offers the possibility of stemming words that
belong to the Moroccan dialectal Arabic.

Samad.stem(word) returns the stem of the input word according to the standard Arabic option.
Samad.stem_di(word) returns the stem of the input word according to the Moroccan Arabic option.

    """
    
    def __init__(self):

        # noun prefixes in standard Arabic
        
        self.noun_pre1= ["\u0627\u0644"]    #["ال"]
        self.noun_pre2= ["\u0644\u0644"]    #["لل"]
        self.noun_pre3= ["\u0628","\u0643"] #["ك","ب"]
        self.noun_pre4= ["\u0641","\u0648"] #["و","ف"]    
        self.noun_pre5= ["\u0644"]          #["ل"]

        # noun suffixes in standard Arabic
                   
        self.noun_suf1=["\u0648\u064A\u062A","\u0648\u064A\u0627\u062A",
                        "\u064A\u0627","\u064A\u062A","\u064A","\u0648",
                        "\u0627","\u0647\u0627\u062A","\u064A\u0627\u062A",
                        "\u0627\u062A","\u062A"]
                        #["ت","ات","يات","هات","ا","و","ي","يت","يا","ويات","ويت"]
                        
        self.noun_suf2=["\u0647","\u0647\u0627","\u0647\u0645\u0627",
                       "\u0647\u0645","\u0647\u0646","\u0643",
                        "\u0643\u064A","\u0643\u0645\u0627",
                       "\u0643\u0645","\u064A","\u0646\u0627"]
                      #["ه","ها","هما","هم","هن","ك","كي","كما","كم", "ي","نا"]
                      
        self.noun_suf3=["\u064A\u0629","\u0648\u0646","\u064A\u0646",
                       "\u064A\u0648\u0646","\u064A\u064A\u0646",
                       "\u062A\u064A\u0646","\u0627\u0646","\u0629",
                       "\u064A\u0627","\u0648\u064A\u0629"]
                       #["ية","ون","ين","يون","يين","تين","ان","ة","يا","وية"]
    
        # verb prefixes in standard Arabic  
                                         
        self.verb_pre1=["\u062A","\u064A","\u0646","\u0627"] 
                                         #["ت","ي","ن","ا"]
        
        self.verb_pre2=["\u0633","\u0644"]   #["س","ل"]
        self.verb_pre3=["\u0648","\u0641"]   #["و","ف"]
        
        # verb suffixes in standard arabic
        
                                                
        self.verb_suf1=["\u0648\u0646","\u0646","\u0627\u0646",
                       "\u064A\u0646","\u062A","\u0627","\u0648"] 
                                #["ون","ن","ان","ين","ت","ا","و"] 
        
                                                         
        self.verb_suf2=["\u064A","\u062A\u0645\u0648","\u062A\u0645\u0627"]
                                                          #["ي","تمو","تما"]
        
        self.verb_suf3=["\u0646\u0627"]   #["نا"]  
        self.verb_suf4=["\u0646\u064A"]   #["ني"]
       
                                         
        self.verb_suf5=["\u0647","\u0647\u0627","\u0647\u0645\u0627",
                        "\u0647\u0645","\u0647\u0646"] 
                                         #["ه","ها","هما","هم","هن"] 
        
                                               
        self.verb_suf6=["\u0643","\u0643\u064A","\u0643\u0645\u0627",
                        "\u0643\u0645"]
                                               #["ك","كي","كما","كم"]            
        
                                                                           
        self.verb_suf7=["\u0648\u0627","\u062A\u0645","\u064A\u0627"]
                                                      #["وا","تم","يا"]

  ## Dialectal Affixes  

        # noun prefixes in Morrocan Arabic
    
        self.di_noun_pre1=["\u0627\u0644"]  #["ال"]
        
                                                 
        self.di_noun_pre2=["\u064A","\u062A","\u062F","\u0639","\u063A"]
                                                 #["ي","ت","د","ع","غ"]  
        
                                                    
        self.di_noun_pre3=["\u0627\u0648","\u0648\u0627","\u0648"]
                                                    #["او","وا","و"]
              
        # noun suffixes in Morrocan Arabic
        
        self.di_noun_suf1=["\u0627\u062A","\u062A"] #["ات","ت"]
        self.di_noun_suf2=["\u0627"]                #["ا"]
        self.di_noun_suf3=["\u064A\u0646"]          #["ين"]
        
                                     
        self.di_noun_suf4=["\u0647\u0645","\u0647\u0648\u0645",
                          "\u0647\u0627","\u0643\u0645","\u0643\u0648\u0645",
                          "\u0643\u064A","\u0643"]
                                     #["هم","هوم","ها","كم","كوم","كي","ك"]
        
        self.di_noun_suf5=["\u0648","\u064A"] #["و","ي"] 
        
                                                   
        self.di_noun_suf6=["\u0647","\u0646\u064A","\u0646\u0627"] 
                                                   #["ه","ني","نا"]
        
        # verb prefixes in Moroccan Arabic
        
                                   
        self.di_verb_pre1=["\u0643\u0627","\u0639\u0627","\u063A\u0627",
                           "\u062A\u0627","\u0643","\u0639","\u063A",
                          "\u062A"]
                          #["كا","عا","غا","تا","ك","ع","غ","ت"]
                                      
        self.di_verb_pre2=["\u0646","\u062A","\u064A"]
                                      #["ن","ت","ي"] 
        
                                                        
        self.di_verb_pre3=["\u0627\u0648","\u0648\u0627","\u0648"]
                                                    #["او","وا","و"]
        
        
        self.di_verb_suf1=["\u0648"]  #["و"]
        
                                                   
        self.di_verb_suf2=["\u064A","\u062A\u064A","\u062A\u0648"]
                                                   #["ي","تي","تو"]
        
                                        
        self.di_verb_suf3=["\u062A","\u0627\u062A"]  #["ات","ت"]
        
        self.di_verb_suf4=["\u0646\u064A"]  #["ني"]
        
        self.di_verb_suf5=["\u0646\u0627"]  #["نا"]
        
        self.di_verb_suf6=["\u0644","\u0644\u064A"] #["لي","ل"]
        
        self.di_verb_suf7=["\u0643","\u0643\u0645","\u0643\u0648\u0645"]
                                                       #["كم","ك","كوم"]
        
                                               
        self.di_verb_suf8=["\u0647","\u0647\u0627","\u0647\u0645",
                           "\u0647\u0648\u0645"] 
                                           #["ه","ها","هوم","هم"]
        
        self.di_verb_suf9=["\u064A","\u064A\u0627"] #["يا","ي"] 
      
       #  negation prefixes in Moroccan Arabic
                                                   
        self.di_neg_pre1=["\u0627\u0648","\u0648\u0627","\u0648"]
                                                   #["او","وا","و"]
        
        self.di_neg_pre2=["\u0645","\u0645\u0627"] #["م","ما"]
        
                                  
        self.di_neg_pre3=["\u0643\u0627","\u0639\u0627","\u063A\u0627",
                           "\u062A\u0627","\u0643","\u0639","\u063A",
                          "\u062A"] 
                                 #["كا","عا","غا","تا","ك","ع","غ","ت"] 
        
        self.di_neg_pre4=["\u0646","\u062A","\u064A"] #["ن","ت","ي"]
        
        # negation suffixes in Moroccan Arabic
        self.di_neg_suf1=["\u0634","\u0634\u064A"] #["شي","ش"]
        
        # post normalisation suffixes 
                                          
        self.post_suf1=["\u0627","\u0648","\u064A","\u064A"]
                                          #["ا","و","ي","ت"]
          
        
        # Combined affixes
        
        self.noun_prefs= self.arrange(self.noun_pref_gen())
        self.noun_suffs= self.arrange(self.noun_suff_gen())
        
        self.verb_prefs= self.arrange(self.verb_pref_gen()) 
        self.verb_suffs= self.arrange(self.verb_suff_gen()) 
        
        self.di_noun_prefs=self.arrange(set(self.di_noun_pref_gen()+self.noun_pref_gen()))
        self.di_noun_suffs=self.arrange(set(self.di_noun_suff_gen()+self.noun_suff_gen()))
        
        self.di_verb_prefs= self.arrange(self.di_verb_pref_gen()) 
        self.di_verb_suffs= self.arrange(set(self.di_verb_suff_gen()+self.verb_suff_gen())) 
        
        self.neg_prefs= self.arrange(self.neg_pref_gen())
        
        self.noun_joined_suffs=self.arrange(self.noun_suf2+self.noun_suf3)
        self.noun_joined_prefs=self.arrange(self.noun_joined_pref_gen())
        
        self.full_suffs=self.arrange(set(self.noun_suff_gen()+self.di_noun_suff_gen()+self.verb_suff_gen()+self.di_verb_suff_gen() ))
        self.full_prefs=self.arrange(set(self.noun_pref_gen()+self.di_noun_pref_gen() +self.verb_pref_gen()+self.di_verb_pref_gen()))
        
        self.standard_suffs=self.arrange(set(self.noun_suff_gen()+self.verb_suff_gen() ))
        self.standard_prefs=self.arrange(set(self.noun_pref_gen()+self.verb_pref_gen() ))
        

    # combining affixes in standard Arabic 
        
    def noun_pref_gen(self):
        """ 
        Generate diffrent combinations of noun prefixes in standard Arabic
        """
        noun_pr=[]
        for p1 in self.noun_pre1:
            noun_pr.append(p1)
            for p3 in self.noun_pre3:
                noun_pr.append(p3+p1)
            for p4 in self.noun_pre4:
                noun_pr.append(p4+p1)
                for p3 in self.noun_pre3:
                    noun_pr.append(p4+p3+p1)
                    
        for p2 in self.noun_pre2:
            noun_pr.append(p2)
            for p4 in self.noun_pre4:
                noun_pr.append(p4+p2)
        return noun_pr
    
    
    def noun_suff_gen(self):
        """ 
        Generate diffrent combinations of noun suffixes in standard Arabic
        """
        noun_su=[]
        for s1 in self.noun_suf1:
            for s2 in self.noun_suf2:    
                noun_su.append(s1+s2)
        noun_su+=self.noun_suf1+self.noun_suf2+ self.noun_suf3       
        return noun_su
     
    def noun_joined_pref_gen(self):
        joined_pr=[]
        for p4 in self.noun_pre4:
            for p5 in self.noun_pre5:
                joined_pr.append(p4+p5)
        joined_pr+=self.noun_pre3+self.noun_pre4+self.noun_pre5
        return joined_pr
    
    
    def verb_pref_gen(self):
        """ 
        Generate diffrent combinations of verb prefixes in standard Arabic
        """
        verb_pr=[]
        for p1 in self.verb_pre1:
            verb_pr.append(p1)
            for p2 in self.verb_pre2:
                verb_pr.append(p2+p1)
                for p3 in self.verb_pre3:
                    verb_pr.append(p3+p2+p1)
            for p3 in self.verb_pre3:
                verb_pr.append(p3+p1)    
        return verb_pr        


    def verb_suff_gen(self):
        """ 
        Generate diffrent combinations of verb suffixes in standard Arabic
        """
        verb_su=[]
        for s1 in self.verb_suf1:
            for s3 in self.verb_suf3:
                verb_su.append(s1+s3)
            for s4 in self.verb_suf4:
                verb_su.append(s1+s4)
            for s5 in self.verb_suf5:
                verb_su.append(s1+s5)
            for s6 in self.verb_suf6:
                verb_su.append(s1+s6)
        
        for s2 in self.verb_suf2:
            for s3 in self.verb_suf3:
                verb_su.append(s2+s3)
            for s4 in self.verb_suf4:    
                verb_su.append(s2+s4)
            for s5 in self.verb_suf5:
                verb_su.append(s2+s5)
            
        for s5 in self.verb_suf5:
            for s3 in self.verb_suf3:
                verb_su.append(s3+s5)
           
        for s6 in self.verb_suf6:
            for s3 in self.verb_suf3:
                verb_su.append(s3+s6)    
                
                
        verb_su+=self.verb_suf1+self.verb_suf2+self.verb_suf5+self.verb_suf6+self.verb_suf7+self.verb_suf3+self.verb_suf4
        return verb_su
        

        
    # combining affixes in Moroccan Arabic
    
    def di_noun_pref_gen(self):
        """ 
        Generate diffrent combinations of noun prefixes in Morrocan Arabic
        """
        di_noun_pr=[]
        for p1 in self.di_noun_pre1:
            for p2 in self.di_noun_pre2:
                di_noun_pr.append(p2+p1)
                for p3 in self.di_noun_pre3:
                    di_noun_pr.append(p3+p2+p1)
        return di_noun_pr   
    
    
    def di_noun_suff_gen(self):
        """ 
        Generate diffrent combinations of noun suffixes in Moroccan Arabic
        """
        di_noun_su=[]

        for s4 in self.di_noun_suf4:
            for s1 in self.di_noun_suf1:
                di_noun_su.append(s1+s4)
            for s2 in self.di_noun_suf2:
                di_noun_su.append(s2+s4)
            for s3 in self.di_noun_suf3:    
                di_noun_su.append(s3+s4)
            
            
        for s5 in self.di_noun_suf5:
            for s1 in self.di_noun_suf1:
                di_noun_su.append(s1+s5)
            for s3 in self.di_noun_suf3:
                di_noun_su.append(s3+s5)    
              
        for s6 in self.di_noun_suf6:
            for s2 in self.di_noun_suf2:
                di_noun_su.append(s2+s6)
        
        di_noun_su+=self.di_noun_suf1+self.di_noun_suf2+self.di_noun_suf3+self.di_noun_suf4+self.di_noun_suf5+self.di_noun_suf6
        return di_noun_su        
            
        
    def di_verb_pref_gen(self):
        """ 
        Generate diffrent combinations of verb prefixes in Morocan Arabic
        """
        di_verb_pr=[]
        for p1 in self.di_verb_pre1:
            for p2 in self.di_verb_pre2:
                di_verb_pr.append(p1+p2)
                for p3 in self.di_verb_pre3:
                    di_verb_pr.append(p3+p1+p2)
        return di_verb_pr      
    

    def di_verb_suff_gen(self):
        """ 
        Generate diffrent combinations of verb suffixes in Moroccan Arabic
        """
        di_verb_su=[]
        
        for s1 in self.di_verb_suf1:
            for s4 in self.di_verb_suf4:
                di_verb_su.append(s1+s4)    
            for s5 in self.di_verb_suf5:
                di_verb_su.append(s1+s5)    
                 
        
        for s6 in self.di_verb_suf6:
            for s5 in self.di_verb_suf5:
                di_verb_su.append(s6+s5)
            for s1 in self.di_verb_suf1:
                di_verb_su.append(s6+s1)
                di_verb_su.append(s1+s6+s1)   
            
        for s2 in self.di_verb_suf2:
            for s4 in self.di_verb_suf4:
                di_verb_su.append(s2+s4)
            for s5 in self.di_verb_suf5:
                di_verb_su.append(s2+s5)
                for s6 in self.di_verb_suf6:
                    di_verb_su.append(s2+s6+s5) 
            for s8 in self.di_verb_suf8:
                di_verb_su.append(s2+s8)
                for s6 in self.di_verb_suf6:
                    di_verb_su.append(s2+s6+s8) 
            for s9 in self.di_verb_suf9:
                for s6 in self.di_verb_suf6:
                    di_verb_su.append(s2+s6+s9) 
            
        for s3 in self.di_verb_suf3:
            for s7 in self.di_verb_suf7:
                di_verb_su.append(s3+s7)
                for s6 in self.di_verb_suf6:
                    di_verb_su.append(s3+s6+s7)  
            for s8 in self.di_verb_suf8:
                di_verb_su.append(s3+s8)
                
            for s6 in self.di_verb_suf6:
                for s9 in self.di_verb_suf9:
                    di_verb_su.append(s3+s6+s9)   
                    
        for s7 in self.di_verb_suf7:
            for s1 in self.di_verb_suf1:
                di_verb_su.append(s1+s7)
            for s5 in self.di_verb_suf5:
                di_verb_su.append(s5+s7)
            for s6 in self.di_verb_suf6:
                di_verb_su.append(s6+s7)
                for s5 in self.di_verb_suf5:
                    di_verb_su.append(s5+s6+s7)    
        
                
        for s8 in self.di_verb_suf8:
            for s1 in self.di_verb_suf1:
                di_verb_su.append(s1+s8)
            for s5 in self.di_verb_suf5:    
                di_verb_su.append(s5+s8)
            for s6 in self.di_verb_suf6:
                di_verb_su.append(s6+s8)
                for s1 in self.di_verb_suf1:
                    di_verb_su.append(s1+s6+s8)
                for s5 in self.di_verb_suf8:
                    di_verb_su.append(s5+s6+s8)
            
        di_verb_su+=self.di_verb_suf1+self.di_verb_suf2+self.di_verb_suf3+self.di_verb_suf4+self.di_verb_suf5+self.di_verb_suf7+self.di_verb_suf8                
        return di_verb_su
    

    def neg_pref_gen(self):
        """ 
        Generate diffrent combinations of negation prefixes in Moroccan arabic
        """
        neg_pr=[]
        for p2 in self.di_neg_pre2:
            for p4 in self.di_neg_pre4:
                neg_pr.append(p2+p4)
                for p3 in self.di_neg_pre3:
                    neg_pr.append(p2+p3+p4)
                    
            for p1 in self.di_neg_pre1:
                    neg_pr.append(p1+p2)
                    for p4 in self.di_neg_pre4:
                        neg_pr.append(p1+p2+p4)
                        for p3 in self.di_neg_pre3: 
                            neg_pr.append(p1+p2+p3+p4) 
            
        neg_pr+=self.di_neg_pre2           
        return neg_pr    
    
    def arrange(self,lst):
        """
        Sort and store affixes by length  
        """
        dc = {}
        for affix in lst:
            if len(affix) not in dc:
                dc[len(affix)] = [affix]
            elif len(affix) in dc:
                dc[len(affix)] += [affix]
                
        ranged = []
        for key in sorted(dc,reverse=True):
            ranged.append(dc[key])
      
        return ranged     
 

    def normalize(self,word):
        """
        normalizing Arabic  characters  
        """
        word=word.replace("\u0623","\u0627")     #("أ", "ا")
        word=word.replace("\u0622","\u0627")     #("آ","ا")
        word=word.replace("\u0625","\u0627")     #("إ","ا")
        word=word.replace("\u0649","\u064A")     #("ى","ي")
        word=word.replace("\u0626","\u064A")     #("ئ","ي")
        word=word.replace("\u0621","\u064A")     #("ء","ي")
        word=word.replace("\u0624","\u0648")     #("ؤ","و")
        return word
    
    
    def pref(self,word,affix):
        """
        remove the prefix from the word 
        """
        
        for prefs in affix:
            if len(word)-len(prefs[0])>=3:
                for pref in prefs:
                    if word.startswith(pref):
                        return word[len(pref):]
        return word
     
        
    def suff(self,word,affix):
        """
        remove the suffix from the word 
        """
        for suffs in affix:
            if len(word)-len(suffs[0])>=3:
                for suff in suffs:
                    if word.endswith(suff):
                        return word[:-len(suff)]
        return word    
    
  
    def pref_tied(self,word,affix_pref, affix_suff):
        """
        remove the prefix from the word depending on the suffix
        """
             
        for suffs in affix_suff:
            if len(word)-len(suffs[0])>=3:
                for suff in suffs:
                    for prefs in affix_pref :
                        if len(word)-len(suffs[0])-len(prefs[0])>=3:
                            for pref in prefs:
                                if word.startswith(pref) and word.endswith(suff):
                                    return word[len(pref):]        
        return word 
        
    
    def negation(self,word):
        """
        remove negation prefix and suffix 
        remove verb prefix and suffix
        """
        affix_pref= self.neg_prefs
        suffs=self.di_neg_suf1
        
        for prefs in affix_pref:
            if len(word)-len(prefs[0])>=3:
                for pref in prefs: 
                    if word.startswith(pref):
                        for suff in suffs:
                            if len(word)-len(prefs[0])-len(suff[0])>=3:
                                if word.endswith(suff):
                                    word=word[len(pref):-len(suff)]
                                    word=self.pref(word,self.di_verb_prefs)
                                    word=self.suff(word,self.full_suffs)
                                    return word            
        return word
    
   
    def post(self,word):
        for suff in self.post_suf1:
            if len(word)-len(suff)>=3:
                if word.endswith(suff):
                    return word[:-len(suff)]
        return word    

                    
    def stem_di(self,word):
        """
        stem the word according to the Morroccan Arabic option of Samad
        """
        
        word=self.normalize(word)
        noun=self.pref(word,self.di_noun_prefs)
        
        if len(noun)<len(word):
            noun=self.suff(noun,self.di_noun_suffs)
            return noun
        
        else:
            verb=self.pref(word,self.di_verb_prefs)
            if len(verb)<len(word):
                verb=self.suff(verb,self.di_verb_suffs)
                return verb
    
            else:
                verb2=self.pref_tied(word,self.verb_prefs,self.verb_suffs)
                if len(verb2)<len(word):
                    verb2=self.suff(verb2,self.di_verb_suffs)
                    return verb2
                
                else:
                    verb_neg=self.negation(word)
                    if len(verb_neg)<len(word):
                        if len(verb_neg)<len(verb):
                            return self.di_neg_pre2[1]+verb_neg
                        
                    else:
                        noun2=self.pref_tied(word,self.noun_joined_prefs,self.noun_suffs)
                        if len(noun2) < len(word):
                            noun2=self.suff(noun2,self.di_noun_suffs)
                            return noun2
                        
                        else:
                            word=self.pref(word,self.full_prefs)
                            word=self.suff(word,self.full_suffs)
                            return word
 

    def stem(self,word):
        
        """
      stem the word  according to the standard Arabic option of Samad
        """
        
        word=self.normalize(word)
        noun=self.pref(word,self.noun_prefs)
        
        if len(noun)<len(word):
            noun=self.suff(noun,self.noun_suffs)
            return noun
        
        else:

            verb2=self.pref_tied(word,self.verb_prefs,self.verb_suffs)
            if len(verb2)<len(word):
                verb2=self.suff(verb2,self.verb_suffs)
                return verb2
    
            else:
                noun2=self.pref_tied(word,self.noun_joined_prefs,self.noun_suffs)
                if len(noun2) < len(word):
                    noun2=self.suff(noun2,self.noun_suffs)
                    return noun2
                    
                else:
                    word=self.pref(word,self.noun_joined_prefs)
                    word=self.suff(word,self.standard_suffs)
                    return word
