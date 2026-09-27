---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: borrower identification scheme
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: system for allocating identifiers to borrowers
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Many banks and other financial institutions have internal systems for assigning identifiers to borrowers. In the
      United States, larger banks may use a Customer Information File (CIF) number, assigned as a part of their federally
      mandated Customer Information Program (CIP).
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  see_also:
  - predicate: http://www.w3.org/2000/01/rdf-schema#seeAlso
    resource: https://www.fincen.gov/resources/statutes-regulations/guidance/guidance-customer-identification-regulations-financial
  subclass_of:
  - concept: /concepts/fibo/FND/Parties/Parties/PartyRoleIdentificationScheme.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Parties/Parties/PartyRoleIdentificationScheme
resource: https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/BorrowerIdentificationScheme
sources:
- id: fibo-source-e2887b268b
  resource: references/fibo/FBC/DebtAndEquities/Debt.rdf
  sha256: e2887b268b4dc9b6c97cf4faa75dafc5e376289f985731b0f89fa10d3254eb07
  title: FIBO source FBC/DebtAndEquities/Debt.rdf
title: borrower identification scheme
type: Ontology Class
---

# borrower identification scheme

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/FBC/DebtAndEquities/Debt/BorrowerIdentificationScheme>

## Definition

system for allocating identifiers to borrowers

## Relationships

- **See also**: [guidance-customer-identification-regulations-financial](<https://www.fincen.gov/resources/statutes-regulations/guidance/guidance-customer-identification-regulations-financial>)
- **Subclass of**: [PartyRoleIdentificationScheme](/concepts/fibo/FND/Parties/Parties/PartyRoleIdentificationScheme.md)

## Annotations

- **label**: borrower identification scheme
- **definition**: system for allocating identifiers to borrowers
- **explanatoryNote**: Many banks and other financial institutions have internal systems for assigning identifiers to borrowers. In the United States, larger banks may use a Customer Information File (CIF) number, assigned as a part of their federally mandated Customer Information Program (CIP).

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
