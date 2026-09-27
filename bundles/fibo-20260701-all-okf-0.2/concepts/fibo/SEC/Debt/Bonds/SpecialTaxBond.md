---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: special tax bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond secured by revenues derived from designated taxes other than ad valorem taxes
  - predicate: http://www.w3.org/2004/02/skos/core#example
    value: For example, bonds for a particular purpose might be supported by sales, cigarette, fuel or business license taxes.
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/SecuredBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SecuredBond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SpecialTaxBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: special tax bond
type: Ontology Class
---

# special tax bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SpecialTaxBond>

## Definition

bond secured by revenues derived from designated taxes other than ad valorem taxes

## Relationships

- **Subclass of**: [MunicipalBond](/concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md)
- **Subclass of**: [SecuredBond](/concepts/fibo/SEC/Debt/Bonds/SecuredBond.md)

## Annotations

- **label**: special tax bond
- **definition**: bond secured by revenues derived from designated taxes other than ad valorem taxes
- **example**: For example, bonds for a particular purpose might be supported by sales, cigarette, fuel or business license taxes.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
