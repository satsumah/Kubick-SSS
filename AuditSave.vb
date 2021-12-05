Private Sub butImprovedSave_Click()
    If IsNull(Me.Initials.Value) Then
        MsgBox ("No initials entered!")
        Exit Sub
    End If
    RunCommand acCmdSaveRecord
    
    Dim SQL As String
    Dim Timestamp As Date
    Timestamp = Now()
    
    SQL = ""
    SQL = SQL & "INSERT INTO AuditLog ([Table], EntryID, EntryType, Initials, [Timestamp])"
    SQL = SQL & " VALUES ("
    SQL = SQL & "'TABLE NAME', "
    SQL = SQL & Me.AutoID.Value & ", "
    SQL = SQL & "'Add Record', "
    SQL = SQL & "'" & Me.Initials.Value & "', "
    SQL = SQL & "#" & Timestamp & "#)"
    MsgBox (SQL)
    CurrentDb.Execute SQL
End Sub
