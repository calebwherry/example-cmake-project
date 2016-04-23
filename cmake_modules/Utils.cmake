########################################
## \file   utils.cmake
## \date   01/01/2014
## \brief  Macro definitions
########################################


#
# Macro to replace item in a list:
#
macro(LIST_REPLACE LIST INDEX NEWVAL)
  list(INSERT ${LIST} ${INDEX} ${NEWVAL})
  math(EXPR __INDEX "${INDEX} + 1")
  list(REMOVE_AT ${LIST} ${__INDEX})
endmacro(LIST_REPLACE)


#
# Function to prepend an item to every item in a list:
#
macro(LIST_PREPEND LIST prepend_val)
  set(LIST ${${LIST}})
  set(index 0)
  list(LENGTH LIST size)
  while(index LESS size)
    list(GET LIST ${index} item)
    LIST_REPLACE(${LIST} ${index} "${prepend_val}/${item}")
    math(EXPR index "${index} + 1")
  endwhile()
endmacro(LIST_PREPEND)
