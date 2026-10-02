---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: borrower identifier
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: sequence of characters, capable of uniquely identifying a borrower
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A given identifier identifies a particular borrower with respect to at least some number of notes/facilities inside
      a particular institution according to some policy for minting identifiers. Optimally, there would be a single identifier
      for a given borrower, but due to operational issues, this is often not the case. A CIF number, or Customer Information
      File number, is used to link accounts across an institution to all notes/facilities owed by a given borrower.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/BorrowerIdentificationScheme
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Designators/isDefinedIn
  - cardinality: 1
    filler: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/Borrower
    kind: exact_qualified_cardinality
    property: https://www.omg.org/spec/Commons/Identifiers/identifies
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.fdic.gov/news/financial-institution-letters/1997/fil9786.pdf
  subclass_of:
  - concept: /concepts/fibo/FND/Parties/Parties/PartyRoleIdentifier.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/PartyRoleIdentifier
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/BorrowerIdentifier
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: borrower identifier
type: Ontology Class
---

# borrower identifier

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/BorrowerIdentifier>

## Definition

sequence of characters, capable of uniquely identifying a borrower

## Relationships

- **See also**: [fil9786.pdf](<https://www.fdic.gov/news/financial-institution-letters/1997/fil9786.pdf>)
- **Subclass of**: [PartyRoleIdentifier](/concepts/fibo/FND/Parties/Parties/PartyRoleIdentifier.md)

## Constraints

- **[isDefinedIn](<https://www.omg.org/spec/Commons/Designators/isDefinedIn>)**: exact qualified cardinality 1 of type [BorrowerIdentificationScheme](/concepts/fibo/FBC/DebtAndEquities/Debt/BorrowerIdentificationScheme.md)
- **[identifies](<https://www.omg.org/spec/Commons/Identifiers/identifies>)**: exact qualified cardinality 1 of type [Borrower](/concepts/fibo/FBC/DebtAndEquities/Debt/Borrower.md)

## Annotations

- **label**: borrower identifier
- **definition**: sequence of characters, capable of uniquely identifying a borrower
- **explanatoryNote**: A given identifier identifies a particular borrower with respect to at least some number of notes/facilities inside a particular institution according to some policy for minting identifiers. Optimally, there would be a single identifier for a given borrower, but due to operational issues, this is often not the case. A CIF number, or Customer Information File number, is used to link accounts across an institution to all notes/facilities owed by a given borrower.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
