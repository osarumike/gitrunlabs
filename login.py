if (rs.next()) {
            if(view.getUsername.equals("Admin"))
            {
               JOptionPane.showMessageDialog(null, "Welcome admin");
            }else
            {
               JOptionPane.showMessageDialog(null, "Welcome user");
            }
        } else {
            JOptionPane.showMessageDialog(null, "Invalid Username or Password", "Access Denied", JOptionPane.ERROR_MESSAGE);
        }
    } catch (Exception e) {
        JOptionPane.showMessageDialog(null, e);
    }

}
