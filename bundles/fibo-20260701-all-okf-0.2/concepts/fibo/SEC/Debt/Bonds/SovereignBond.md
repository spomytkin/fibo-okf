---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: sovereign bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond issued by the government of a country
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Sovereign bonds issued by G20 developed countries are generally full faith and credit obligations. Sovereign bonds
      issued by emerging and developing countries may be issued in local currency or a G7 currency, and may either be full
      faith and credit (unsecured) or secured.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/GovernmentBond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GovernmentBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/SovereignDebtInstrument.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SovereignDebtInstrument
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SovereignBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: sovereign bond
type: Ontology Class
---

# sovereign bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/SovereignBond>

## Definition

bond issued by the government of a country

## Relationships

- **Subclass of**: [GovernmentBond](/concepts/fibo/SEC/Debt/Bonds/GovernmentBond.md)
- **Subclass of**: [SovereignDebtInstrument](/concepts/fibo/SEC/Debt/Bonds/SovereignDebtInstrument.md)

## Constraints

- **Disjoint with**: [MunicipalBond](/concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md)

## Annotations

- **label**: sovereign bond
- **definition**: bond issued by the government of a country
- **explanatoryNote**: Sovereign bonds issued by G20 developed countries are generally full faith and credit obligations. Sovereign bonds issued by emerging and developing countries may be issued in local currency or a G7 currency, and may either be full faith and credit (unsecured) or secured.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
