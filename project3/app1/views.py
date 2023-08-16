from django.shortcuts import render

def contact(request):
    return render(request, './index2.html', context={'courses':[
        {
            'id':1,
            'name':'c',
            'teacher':'rahim',
        },
        {
            'id':2,
            'name':'c++',
            'teacher':'kahim',
        },
        {
            'id':3,
            'name':'c#',
            'teacher':'fahim',
        }
        ]
        }
                  )
