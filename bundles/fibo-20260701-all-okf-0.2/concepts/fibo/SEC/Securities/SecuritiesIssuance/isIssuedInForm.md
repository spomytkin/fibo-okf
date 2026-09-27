---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is issued in form
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates the form in which the security is issued, typically in registered form
  domain:
  - concept: /concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/FBC/FinancialInstruments/FinancialInstruments/Security
  range:
  - concept: /concepts/fibo/SEC/Securities/SecuritiesIssuance/SecurityForm.md
    predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/SecurityForm
  rdf_types:
  - http://www.w3.org/2002/07/owl#ObjectProperty
  subproperty_of:
  - concept: /concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Agreements/Contracts/isEvidencedBy
  - concept: /concepts/fibo/FND/Relations/Relations/isExemplifiedBy.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subPropertyOf
    resource: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isExemplifiedBy
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isIssuedInForm
sources:
- id: fibo-source-7b3088e831
  resource: references/fibo/SEC/Securities/SecuritiesIssuance.rdf
  sha256: 7b3088e8315beedb43222e345522bb546f87fbbd6850833103c9ba84ea1d7ac0
  title: FIBO source SEC/Securities/SecuritiesIssuance.rdf
title: is issued in form
type: Ontology Property
---

# is issued in form

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Securities/SecuritiesIssuance/isIssuedInForm>

## Definition

indicates the form in which the security is issued, typically in registered form

## Relationships

- **Domain**: [Security](/concepts/fibo/FBC/FinancialInstruments/FinancialInstruments/Security.md)
- **Range**: [SecurityForm](/concepts/fibo/SEC/Securities/SecuritiesIssuance/SecurityForm.md)
- **Subproperty of**: [isEvidencedBy](/concepts/fibo/FND/Agreements/Contracts/isEvidencedBy.md)
- **Subproperty of**: [isExemplifiedBy](/concepts/fibo/FND/Relations/Relations/isExemplifiedBy.md)

## Annotations

- **label**: is issued in form
- **definition**: indicates the form in which the security is issued, typically in registered form

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
