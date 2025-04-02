# Executes a command to kill a specific process
exec { 'killmenow':
  command => 'pkill killmenow'
} 