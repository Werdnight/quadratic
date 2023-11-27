from main import main
from pytest import *


def test_1():
    answer = main('0 0 0')
    assert answer == 'Любое число'


def test_2():
    answer = main('0 0 1')
    assert answer == "Корней нет"


def test_3():
    answer = main('0 1 0')
    assert answer == '0'


def test_4():
    answer = main('1 0 0')
    assert answer == '0\n0'


def test_4_1():
    answer = main('-897.456 0 0')
    assert answer == '0\n0'


def test_5():
    answer = main('0 1 1')
    assert answer == '-1'


def test_6():
    answer = main('1 1 0')
    assert answer == '-1\n0'


def test_7():
    answer = main('1 0 1')
    assert answer == '-i\ni'


def test_8():
    answer = main('1 45 0')
    assert answer == '-4.5e1\n0'


def test_9():
    answer = main('2e-10 2e-10 1e-10')
    assert answer == '-5e-1-5e-1i\n-5e-1+5e-1i'


def test_10():
    answer = main('2 2 1')
    assert answer == '-5e-1-5e-1i\n-5e-1+5e-1i'


def test_11():
    answer = main('10000 70000 120000')
    assert answer == '-4\n-3'


def test_12():
    answer = main('0.0001 0.0007 0.0012')
    assert answer == '-4\n-3'


def test_13():
    answer = main('5 100 -10.05')
    assert answer == '-2.01e1\n1e-1'


def test_14():
    answer = main('1 -30 221')
    assert answer == '1.3e1\n1.7e1'


def test_15():
    answer = main('@ inf +')
    assert answer == f'Неправильный ввод'


def test_16():
    answer = main('` 9 inf')
    assert answer == f'Неправильный ввод'


def test_17():
    answer = main('  nan  ')
    assert answer == f'Неправильный ввод'


def test_18():
    answer = main('1 11 0')
    assert answer == '-1.1e1\n0'


def test_19():
    answer = main('1 0 25')
    assert answer == '-5i\n5i'


def test_20():
    answer = main('-1 0 -25')
    assert answer == '-5i\n5i'


def test_21():
    answer = main('-1 0 25')
    assert answer == '-5\n5'


def test_22():
    answer = main('1 0 -25')
    assert answer == '-5\n5'


def test_23():
    answer = main('0 5 25')
    assert answer == '-5'


def test_24():
    answer = main('0 5 -25')
    assert answer == '5'


def test_25():
    answer = main('0 -5 -25')
    assert answer == '-5'


def test_26():
    answer = main('nan nan inf')
    assert answer == 'nan\nnan'


def test_27():
    answer = main('nan nan nan')
    assert answer == 'nan\nnan'


def test_28():
    answer = main('inf inf inf')
    assert answer == 'nan\nnan'


def test_29():
    answer = main('2 1 inf')
    assert answer == 'nan\nnan'


def test_30():
    answer = main('3 nan inf')
    assert answer == 'nan\nnan'


def test_31():
    answer = main('+1 nan -1.23')
    assert answer == 'nan\nnan'


def test_32():
    answer = main('2 2 -420')
    assert answer == '-1.5e1\n1.4e1'


def test_33():
    answer = main('-1 5 36')
    assert answer == '-4\n9'


def test_34():
    answer = main('-4 32 -28')
    assert answer == '1\n7'


def test_35():
    answer = main('3 -15 -198') #?
    assert answer == '-6\n1.1e1'


def test_36():
    answer = main('-2 -18 -36')
    assert answer == '-6\n-3'


def test_37():
    answer = main('6 -27 12')
    assert answer == '5e-1\n4'


def test_38():
    answer = main('2 -9 4')
    assert answer == '5e-1\n4'


def test_39():
    answer = main('200 -900 400')
    assert answer == '5e-1\n4'


def test_40():
    answer = main('2e2 -9e2 4e2')
    assert answer == '5e-1\n4'


def test_41():
    answer = main('0.5 1 0.5')
    assert answer == '-1\n-1'


def test_42():
    answer = main('5e-1 1e0 5e-1')
    assert answer == '-1\n-1'


def test_43():
    answer = main('1e100 0 1e100') #?
    assert answer == '-i\ni'


def test_44():
    answer = main('-1 +7 18')
    assert answer == '-2\n9'


def test_45():
    answer = main('10000 20000 10000')
    assert answer == '-1\n-1'


def test_46():
    answer = main('50 10 -40')
    assert answer == '-1\n8e-1'


def test_47():
    answer = main('2 7 0')
    assert answer == '-3.5\n0'


def test_48():
    answer = main('1 2 -3')
    assert answer == '-3\n1'


def test_49():
    answer = main('2 -11 5')
    assert answer == '5e-1\n5'


def test_50():
    answer = main('2 5 -3')
    assert answer == '-3\n5e-1'


def test_51():
    answer = main('1 -5 6')
    assert answer == '2\n3'


def test_52():
    answer = main('1e100 -5e100 6e100')
    assert answer == '2\n3'


def test_53():
    answer = main('+1. -17. +16.')
    assert answer == '1\n1.6e1'


def test_54():
    answer = main('1 12 36')
    assert answer == '-6\n-6'


def test_55():
    answer = main('5 7 2')
    assert answer == '-1\n-4e-1'


def test_56():
    answer = main('4 -12 9')
    assert answer == '1.5\n1.5'


def test_57():
    answer = main('1 -6 34')
    assert answer == '3-5i\n3+5i'


def test_58():
    answer = main('1 2 5')
    assert answer == '-1-2i\n-1+2i'


def test_59():
    answer = main('1 -16 100')
    assert answer == '8-6i\n8+6i'


def test_60():
    answer = main('1 -4 13')
    assert answer == '2-3i\n2+3i'


def test_61():
    answer = main('1 -3 8.5')
    assert answer == '1.5-2.5i\n1.5+2.5i'


def test_62():
    answer = main('1.0 1. .0')
    assert answer == '-1\n0'


def test_63():
    answer = main('1.0 1. 0.')
    assert answer == '-1\n0'


def test_64():
    answer = main('1.0e0 1.e0 0.e0')
    assert answer == '-1\n0'

def test1_quadratic():
    test = main('0 0 0')
    assert test == 'Любое число' #+

def test2_quadratic():
    test = main('0 0 1')
    assert test == 'Корней нет' #+

def test3_quadratic():
    test = main('0 1 0')
    assert test == '0' #+

def test4_quadratic():
    test = main('1 0 0')
    assert test == '0\n0'#+

def test5_quadratic():
    test = main('0 1 1')
    assert test == '-1'#+

def test6_quadratic():
    test = main('1 1 0')
    assert test == '-1\n0'#+

def test7_quadratic():
    test = main('1 0 1')
    assert test == '-i\ni'

def test8_quadratic():
    test = main('1 45 0')
    assert test == '-4.5e1\n0'

def test9_quadratic():
    test = main('2e-10 2e-10 1e-10')
    assert test == '-5e-1-5e-1i\n-5e-1+5e-1i'

def test10_quadratic():
    test = main('2 2 1')
    assert test == '-5e-1-5e-1i\n-5e-1+5e-1i'

def test11_quadratic():
    test = main('10000 70000 120000')
    assert test == '-4\n-3' #+

def test12_quadratic():
    test = main('0.0001 0.0007 0.0012')
    assert test == '-4\n-3' #+

def test13_quadratic():
    test = main('5 100 -10.05')
    assert test == '-2.01e1\n1e-1' #+

def test14_quadratic():
    test = main('1 -30 221')
    assert test == '1.3e1\n1.7e1'#+

def test15_quadratic():
    test = main('@ inf +')
    assert test == 'Неправильный ввод'#+

def test16_quadratic():
    test = main('` 9 inf')
    assert test == 'Неправильный ввод'#+

def test17_quadratic():
    test = main('  nan  ')
    assert test == 'Неправильный ввод'

def test18_quadratic():
    test = main('1 11 0')
    assert test == '-1.1e1\n0'

def test19_quadratic():
    test = main('1 0 25')
    assert test == '-5i\n5i'

def test20_quadratic():
    test = main('-1 0 -25')
    assert test == '-5i\n5i'

def test21_quadratic():
    test = main('-1 0 25')
    assert test == '-5\n5'

def test22_quadratic():
    test = main('1 0 -25')
    assert test == '-5\n5'

def test23_quadratic():
    test = main('1 -1 1')
    assert test == '5e-1-8.660254037844386467637231707529361834714026269051903140279034897259' \
                                       '6650845440001854057309337862428783e-1i\n5e-1+8.660254037844386467637231707' \
                                       '5293618347140262690519031402790348972596650845440001854057309337862428783e-1i'

def test24_quadratic():
    test = main('2 2 3')
    assert test == '-5e-1-1.11803398874989484820458683436563811772030917980576286213544862270' \
                                       '52604628189024497072072041893911374i\n-5e-1+1.118033988749894848204586834' \
                                       '3656381177203091798057628621354486227052604628189024497072072041893911374i'

def test25_quadratic():
    test = main('nan nan nan')
    assert test == 'nan\nnan'

def test26_quadratic():
    test = main('2 inf 3')
    assert test == 'nan\nnan'

def test36_quadratic():
    test = main('1e1000 1e100 0')
    assert test == '-1e-900\n0'

def test37_quadratic():
    test = main('1e-1000 1e-1000 0')
    assert test == '-1\n0'


def test27_quadratic():
    test = main('1 1 1')
    assert test == '-5e-1-8.660254037844386467637231707529361834714026269051903140279034897259' \
                                       '6650845440001854057309337862428783e-1i\n-5e-1+8.660254037844386467637231707' \
                                       '5293618347140262690519031402790348972596650845440001854057309337862428783e-1i'

def test28_quadratic():
    test = main('4 0 -12')
    assert test == '-1.73205080756887729352744634150587236694280525381038062805580697945193301' \
                                       '69088000370811461867572485756\n1.73205080756887729352744634150587236694280' \
                                       '52538103806280558069794519330169088000370811461867572485756'

def test29_quadratic():
    test = main('-8 10 5')
    assert test == '-3.82782218537318706545826653787971391391799538201071673492074048657984368' \
                                       '87821102537001928333965383045e-1\n1.63278221853731870654582665378797139139' \
                                       '17995382010716734920740486579843688782110253700192833396538304'

def test30_quadratic():
    test = main('3 -12 3')
    assert test == '2.679491924311227064725536584941276330571947461896193719441930205480669830' \
                                       '9119996291885381324275142432e-1\n3.732050807568877293527446341505872366942' \
                                       '8052538103806280558069794519330169088000370811461867572485756'

def test31_quadratic():
    test = main('-6 9 1')
    assert test == '-1.03912563829966531935086556710087665894586055287902744128498208324195665' \
                                       '47544617274393596903154556141e-1\n1.60391256382996653193508655671008766589' \
                                       '45860552879027441284982083241956654754461727439359690315455614'

def test32_quadratic():
    test = main('3 7 1')
    assert test == '-2.18046042171636994816661404086701117701416168246440186440319217441438878' \
                                       '75531517066338444046596414439\n-1.5287291161696338516671929246632215631917' \
                                       '165086893146893014115891894454578018162669948892867369188942e-1'

def test33_quadratic():
    test = main('12 5 3')
    assert test == '-2.08333333333333333333333333333333333333333333333333333333333333333333333' \
                                       '33333333333333333333333333333e-1-4.545296714431547671459231036405375780335' \
                                       '4723761227598970903103728493036562904852067212275265636113083e-1i\n-2.0833' \
                                       '33333333333333333333333333333333333333333333333333333333333333333333333333' \
                                       '3333333333333333333333e-1+4.5452967144315476714592310364053757803354723761' \
                                       '227598970903103728493036562904852067212275265636113083e-1i'

def test39_quadratic():
    test = main('1e999 2e999 1e999')
    assert test == '-1\n-1'

def test35_quadratic():
    test = main('10203.02001   0.030407   10.0201002')
    assert test == '-1.4900980283385722772879282043082065855911224465000338659533806010834237303' \
                                       '431496455528366644847930666e-6-3.1338027876485327042115404840459476122456666' \
                                       '539388139108061143315869694467592583149570323909249707946e-2i\n-1.4900980283' \
                                       '3857227728792820430820658559112244650003386595338060108342373034314964555283' \
                                       '66644847930666e-6+3.13380278764853270421154048404594761224566665393881391080' \
                                       '61143315869694467592583149570323909249707946e-2i'

def test38_quadratic():
    test = main('1e10000 1e10000 1e10000')
    assert test == '-5e-1-8.660254037844386467637231707529361834714026269051903140279034897259' \
                                       '6650845440001854057309337862428783e-1i\n-5e-1+8.660254037844386467637231707' \
                                       '5293618347140262690519031402790348972596650845440001854057309337862428783e-1i'



def test40_quadratic():
    test = main('1e-123 1e-456 1e-789')
    assert test == '-5e-334-8.660254037844386467637231707529361834714026269051903140279034897' \
                                       '2596650845440001854057309337862428783e-334i\n-5e-334+8.6602540378443864676' \
                                       '3723170752936183471402626905190314027903489725966508454400018540573093378' \
                                       '62428783e-334i'

def test41_quadratic():
    test = main('1e-678 1e-915 1e-456')
    assert test == '-5e-238-9.999999999999999999999999999999999999999999999999999999999999999' \
                                       '9999999999999999999999999999999999999e110i\n-5e-238+9.9999999999999999999' \
                                       '9999999999999999999999999999999999999999999999999999999999999999999999999' \
                                       '99999999e110i'
def test42_quadratic():
    test = main('1.23e-998 9.80e-1003 1.234e1004')
    assert test == '-3.983739837398373983739837398373983739837398373983739837398373983739837' \
                                       '3983739837398373983739837398373e-5-1.00162469644090006495688463588272895' \
                                       '41562323529463761543035191250399826423751686174701581991702771264e1001i' \
                                       '\n-3.983739837398373983739837398373983739837398373983739837398373983739' \
                                       '8373983739837398373983739837398373e-5+1.0016246964409000649568846358827' \
                                       '289541562323529463761543035191250399826423751686174701581991702771264e1' \
                                       '001i'

def test34_quadratic():
    test = main('1234567890'*100 + ' ' + '1234567890'*100 + ' ' + '1234567890'*100)
    assert test == '-5e-1-8.66025403784438646763723170752936183471402626905190314027903489725966' \
                                       '50845440001854057309337862428783e-1i\n-5e-1+8.660254037844386467637231707529' \
                                       '3618347140262690519031402790348972596650845440001854057309337862428783e-1i'


