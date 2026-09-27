---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: corporate officer
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: high-level management executive of a corporation or other organization, hired by the board of directors or the
      business owner(s), charged with certain operational responsibilities, and who has the authority to act on behalf of
      the organization, including the authority to enter into contracts on behalf of the organization
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: Corporate officers may include a Chief Executive Officer (CEO), Chief Financial Officer (CFO), president, vice
      president(s), and in some cases a Chief Operating Officer (COO), Chief Compliance Officer (CCO), or other executive
      responsible for a critical function in the organization.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: In banking, corporate officers have the legal capacity to execute some documents and make certain decisions on
      behalf of the institution due to the nature of the business. The level of authority varies depending on the role the
      officer plays, however, and based on bank policy. In large institutions, corporate officers may include loan/lending
      officers, those in certain supervisory roles, and others with varying degrees of authority, and frequently they are
      given a 'vice president' title, particularly if they are customer facing. Hiring and other decisions related to such
      corporate officers may be delegated to more operational levels, rather than by the board directly, with respect to such
      personnel.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that in most cases in the United States, corporate officers, especially those with signatory capacity and
      other fiduciary responsibilities must be employees, especially with respect to financial institutions and other highly
      regulated domains. There are cases, however, when an independent contractor or professional services provider may play
      the role of a corporate officer, such as a 'CFO for hire', which is a common practice in start-up organizations.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/Executive.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Executive
  - concept: /concepts/fibo/BE/OwnershipAndControl/Executives/Signatory.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/Signatory
  - predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://www.omg.org/spec/Commons/Organizations/OrganizationMember
resource: https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/CorporateOfficer
sources:
- id: fibo-source-27c89de7b6
  resource: references/fibo/BE/OwnershipAndControl/Executives.rdf
  sha256: 27c89de7b6ec909d26a0a73d1d2b7cbaadf425eb5e6a488f681cc3eba80f91ca
  title: FIBO source BE/OwnershipAndControl/Executives.rdf
title: corporate officer
type: Ontology Class
---

# corporate officer

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/BE/OwnershipAndControl/Executives/CorporateOfficer>

## Definition

high-level management executive of a corporation or other organization, hired by the board of directors or the business owner(s), charged with certain operational responsibilities, and who has the authority to act on behalf of the organization, including the authority to enter into contracts on behalf of the organization

## Relationships

- **Subclass of**: [Executive](/concepts/fibo/BE/OwnershipAndControl/Executives/Executive.md)
- **Subclass of**: [Signatory](/concepts/fibo/BE/OwnershipAndControl/Executives/Signatory.md)
- **Subclass of**: [OrganizationMember](<https://www.omg.org/spec/Commons/Organizations/OrganizationMember>)

## Annotations

- **label**: corporate officer
- **definition**: high-level management executive of a corporation or other organization, hired by the board of directors or the business owner(s), charged with certain operational responsibilities, and who has the authority to act on behalf of the organization, including the authority to enter into contracts on behalf of the organization
- **example**: Corporate officers may include a Chief Executive Officer (CEO), Chief Financial Officer (CFO), president, vice president(s), and in some cases a Chief Operating Officer (COO), Chief Compliance Officer (CCO), or other executive responsible for a critical function in the organization.
- **explanatoryNote**: In banking, corporate officers have the legal capacity to execute some documents and make certain decisions on behalf of the institution due to the nature of the business. The level of authority varies depending on the role the officer plays, however, and based on bank policy. In large institutions, corporate officers may include loan/lending officers, those in certain supervisory roles, and others with varying degrees of authority, and frequently they are given a 'vice president' title, particularly if they are customer facing. Hiring and other decisions related to such corporate officers may be delegated to more operational levels, rather than by the board directly, with respect to such personnel.
- **explanatoryNote**: Note that in most cases in the United States, corporate officers, especially those with signatory capacity and other fiduciary responsibilities must be employees, especially with respect to financial institutions and other highly regulated domains. There are cases, however, when an independent contractor or professional services provider may play the role of a corporate officer, such as a 'CFO for hire', which is a common practice in start-up organizations.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
