---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: is bank qualified
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: indicates whether or not a given municipal bond conforms with section 265(b)(3) of the IRS tax code; when purchased
      by a commercial bank for its portfolio, such designation allows the bank to deduct a portion of the interest cost of
      carry for the position
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: A bond that is bank qualified is also known as a qualified tax-exempt obligation.
  domain:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#domain
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
  range:
  - predicate: http://www.w3.org/2000/01/rdf-schema#range
    resource: http://www.w3.org/2001/XMLSchema#boolean
  rdf_types:
  - http://www.w3.org/2002/07/owl#DatatypeProperty
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/isBankQualified
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: is bank qualified
type: Ontology Property
---

# is bank qualified

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/isBankQualified>

## Definition

indicates whether or not a given municipal bond conforms with section 265(b)(3) of the IRS tax code; when purchased by a commercial bank for its portfolio, such designation allows the bank to deduct a portion of the interest cost of carry for the position

## Relationships

- **Domain**: [MunicipalBond](/concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md)
- **Range**: [boolean](<http://www.w3.org/2001/XMLSchema#boolean>)

## Annotations

- **label**: is bank qualified
- **definition**: indicates whether or not a given municipal bond conforms with section 265(b)(3) of the IRS tax code; when purchased by a commercial bank for its portfolio, such designation allows the bank to deduct a portion of the interest cost of carry for the position
- **explanatoryNote**: A bond that is bank qualified is also known as a qualified tax-exempt obligation.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
