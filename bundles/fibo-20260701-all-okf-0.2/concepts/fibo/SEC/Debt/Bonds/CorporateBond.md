---
owl:
  annotations:
  - predicate: http://www.w3.org/2000/01/rdf-schema#label
    value: corporate bond
  - predicate: http://www.w3.org/2004/02/skos/core#definition
    value: bond issued by a company in order to raise financing
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Corporate bonds are issued for purposes such as mergers and acquisitions, business expansion, or to cover ongoing
      operational needs, and are typically longer-term debt instruments that have a maturity of at least one year. Corporate
      debt instruments with maturity shorter than one year are referred to as commercial paper.
  - predicate: https://www.omg.org/spec/Commons/AnnotationVocabulary/explanatoryNote
    value: Note that some classification schemes consider any bond except those issued by a government in its own currency
      to be a corporate bond, for example, a bond issued by Canada in US dollars might be classified as a corporate bond.
      Bonds issued by multinational / supranational organizations such as the European Bank for Reconstruction and Development
      (EBRD) may also be considered corporate bonds rather than government bonds.
  disjoint_with:
  - concept: /concepts/fibo/SEC/Debt/Bonds/GovernmentBond.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/GovernmentBond
  - concept: /concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md
    predicate: http://www.w3.org/2002/07/owl#disjointWith
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/MunicipalBond
  rdf_types:
  - http://www.w3.org/2002/07/owl#Class
  restrictions:
  - kind: some_values_from
    property: https://spec.edmcouncil.org/fibo/ontology/FND/Relations/Relations/isIssuedBy
    value: Nfb8c87f6678b4e4a93e924057b5f34e9
  subclass_of:
  - concept: /concepts/fibo/SEC/Debt/Bonds/Bond.md
    predicate: http://www.w3.org/2000/01/rdf-schema#subClassOf
    resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/Bond
resource: https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CorporateBond
sources:
- id: fibo-source-e8d406159e
  resource: references/fibo/SEC/Debt/Bonds.rdf
  sha256: e8d406159e34a92dc8e87cfce162f6fc67e075db2b2f73c520d41f7419bb0844
  title: FIBO source SEC/Debt/Bonds.rdf
title: corporate bond
type: Ontology Class
---

# corporate bond

Canonical resource: <https://spec.edmcouncil.org/fibo/ontology/SEC/Debt/Bonds/CorporateBond>

## Definition

bond issued by a company in order to raise financing

## Relationships

- **Subclass of**: [Bond](/concepts/fibo/SEC/Debt/Bonds/Bond.md)

## Constraints

- **Disjoint with**: [GovernmentBond](/concepts/fibo/SEC/Debt/Bonds/GovernmentBond.md)
- **Disjoint with**: [MunicipalBond](/concepts/fibo/SEC/Debt/Bonds/MunicipalBond.md)
- **[isIssuedBy](/concepts/fibo/FND/Relations/Relations/isIssuedBy.md)**: some values from value `Nfb8c87f6678b4e4a93e924057b5f34e9`

## Annotations

- **label**: corporate bond
- **definition**: bond issued by a company in order to raise financing
- **explanatoryNote**: Corporate bonds are issued for purposes such as mergers and acquisitions, business expansion, or to cover ongoing operational needs, and are typically longer-term debt instruments that have a maturity of at least one year. Corporate debt instruments with maturity shorter than one year are referred to as commercial paper.
- **explanatoryNote**: Note that some classification schemes consider any bond except those issued by a government in its own currency to be a corporate bond, for example, a bond issued by Canada in US dollars might be classified as a corporate bond. Bonds issued by multinational / supranational organizations such as the European Bank for Reconstruction and Development (EBRD) may also be considered corporate bonds rather than government bonds.

## Source fidelity

The complete RDF/OWL statements for this resource are retained in the source document referenced by the `sources` frontmatter. The `owl` frontmatter extension carries the profile's structured projection of relationships, restrictions, characteristics, and annotations.
