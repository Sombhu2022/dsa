
public class LinkListExample{

    class Node{
        int data ; 
        Node next;
        Node(int data){
            this.data=data;
            this.next = null;
        }
    }
    Node head;

    //add first position 
    void addFirst(int data){
        Node newNode = new Node(data);
        if(head == null){
            head = newNode;
            return ;
        }

        newNode.next=head;
        head = newNode;
    }

    // add last position 
    void addLast(int data){
        Node newNode = new Node(data);
        if(head == null){
            head = newNode;
            return;
        }

        Node currNode = head;
        while (currNode.next != null) {
            currNode = currNode.next;
        }
        currNode.next = newNode;
    }

    // print LinkList 
    void printLinkList(){
        if(head == null){
            System.out.println("Link list is empty ");
            return ;
        }
        Node cuurNode = head;
        while (cuurNode != null) {
            System.out.print(cuurNode.data+ " -> ");
            cuurNode= cuurNode.next;
        }
        System.out.println("NULL");
    }

    //delete - first position
    void deleteFirst(){
         if(head == null){
            System.out.println("Link list is empty ");
            return ;
        }
        Node currNode = head;
        head = currNode.next;
        
    }
    // delete - last Position 
    void deleteLast(){
        if(head == null){
            System.out.println("Link list is empty ");
            return ;
        }
        Node lastNode = head.next;
        Node secondLast = head;
        if(lastNode.next != null){
            lastNode = lastNode.next;
            secondLast=secondLast.next;
        }
        secondLast.next = null;
    }

    public static void main(String[] args) {

        LinkListExample linkList = new LinkListExample();
        linkList.printLinkList();
        linkList.addFirst(34);
        linkList.addFirst(90);
        linkList.addLast(20);
        linkList.printLinkList();
        linkList.deleteFirst();
        linkList.printLinkList();
        linkList.deleteLast();
        linkList.printLinkList();
        
    }
}